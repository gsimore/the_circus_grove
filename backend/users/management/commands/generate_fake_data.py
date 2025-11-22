"""
Management command to generate fake data for local development.
Creates fake users, training sessions, meals, check-ins, and plans.
"""
from datetime import datetime, timedelta, time
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import random

from training.models import TrainingSession, Exercise, TrainingPlan, TrainingPlanExercise
from nutrition.models import Meal, Food, NutritionPlan, NutritionPlanMeal
from checkins.models import CheckIn


User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake data for local development (5-10 instances per collection)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before generating new data',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            self.clear_data()

        self.stdout.write('Generating fake data...')
        
        # Generate users (coaches and normal users)
        coaches = self.generate_coaches(3)
        users = self.generate_users(7, coaches)
        all_users = coaches + users
        
        # Generate training data
        self.generate_training_sessions(all_users, 8)
        self.generate_training_plans(coaches, users, 3)
        
        # Generate nutrition data
        self.generate_meals(all_users, 8)
        self.generate_nutrition_plans(coaches, users, 3)
        
        # Generate check-ins
        self.generate_checkins(all_users, 8)
        
        self.stdout.write(self.style.SUCCESS('Successfully generated fake data!'))
        self.stdout.write(f'Created:')
        self.stdout.write(f'  - {len(coaches)} coaches')
        self.stdout.write(f'  - {len(users)} normal users')
        self.stdout.write(f'  - {TrainingSession.objects.count()} training sessions')
        self.stdout.write(f'  - {Exercise.objects.count()} exercises')
        self.stdout.write(f'  - {TrainingPlan.objects.count()} training plans')
        self.stdout.write(f'  - {TrainingPlanExercise.objects.count()} training plan exercises')
        self.stdout.write(f'  - {Meal.objects.count()} meals')
        self.stdout.write(f'  - {Food.objects.count()} food items')
        self.stdout.write(f'  - {NutritionPlan.objects.count()} nutrition plans')
        self.stdout.write(f'  - {NutritionPlanMeal.objects.count()} nutrition plan meals')
        self.stdout.write(f'  - {CheckIn.objects.count()} check-ins')

    def clear_data(self):
        """Clear all fake data (keep superusers)."""
        User.objects.filter(is_superuser=False).delete()
        TrainingSession.objects.all().delete()
        Exercise.objects.all().delete()
        TrainingPlan.objects.all().delete()
        TrainingPlanExercise.objects.all().delete()
        Meal.objects.all().delete()
        Food.objects.all().delete()
        NutritionPlan.objects.all().delete()
        NutritionPlanMeal.objects.all().delete()
        CheckIn.objects.all().delete()

    def generate_coaches(self, count):
        """Generate coach users."""
        coaches = []
        for i in range(count):
            username = f"coach_{fake.user_name()}_{i}"
            email = f"coach{i}@{fake.domain_name()}"
            coach = User.objects.create_user(
                username=username,
                email=email,
                password='password123',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number()[:20],  # Limit to 20 characters
                bio=fake.text(max_nb_chars=200),
                date_of_birth=fake.date_of_birth(minimum_age=25, maximum_age=50),
                height_cm=Decimal(str(round(random.uniform(160, 195), 2))),
                user_type='coach'
            )
            coaches.append(coach)
            self.stdout.write(f'Created coach: {coach.username}')
        return coaches

    def generate_users(self, count, coaches):
        """Generate normal users."""
        users = []
        for i in range(count):
            username = f"user_{fake.user_name()}_{i}"
            email = f"user{i}@{fake.domain_name()}"
            coach = random.choice(coaches) if random.random() > 0.3 else None
            user = User.objects.create_user(
                username=username,
                email=email,
                password='password123',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number()[:20],  # Limit to 20 characters
                bio=fake.text(max_nb_chars=200),
                date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=60),
                height_cm=Decimal(str(round(random.uniform(150, 200), 2))),
                user_type='normal',
                coach=coach
            )
            users.append(user)
            self.stdout.write(f'Created user: {user.username}')
        return users

    def generate_training_sessions(self, users, count):
        """Generate training sessions with exercises."""
        intensities = ['low', 'medium', 'high']
        exercise_names = [
            'Bench Press', 'Squat', 'Deadlift', 'Shoulder Press', 'Pull-ups',
            'Barbell Row', 'Dumbbell Curl', 'Tricep Extension', 'Leg Press',
            'Lunges', 'Lateral Raise', 'Face Pull', 'Cable Fly', 'Leg Curl'
        ]
        
        for _ in range(count):
            user = random.choice(users)
            date = fake.date_between(start_date='-30d', end_date='today')
            
            session = TrainingSession.objects.create(
                user=user,
                title=fake.catch_phrase(),
                description=fake.text(max_nb_chars=200),
                date=date,
                duration_minutes=random.randint(30, 120),
                intensity=random.choice(intensities),
                calories_burned=random.randint(200, 800),
                notes=fake.text(max_nb_chars=150) if random.random() > 0.5 else None
            )
            
            # Add 3-6 exercises per session
            for _ in range(random.randint(3, 6)):
                Exercise.objects.create(
                    session=session,
                    name=random.choice(exercise_names),
                    sets=random.randint(2, 5),
                    reps=random.randint(6, 15),
                    weight_kg=Decimal(str(round(random.uniform(10, 150), 2))),
                    rest_seconds=random.choice([30, 60, 90, 120]),
                    notes=fake.sentence() if random.random() > 0.7 else None
                )

    def generate_training_plans(self, coaches, users, count):
        """Generate training plans with exercises."""
        exercise_names = [
            'Bench Press', 'Squat', 'Deadlift', 'Shoulder Press', 'Pull-ups',
            'Barbell Row', 'Dumbbell Curl', 'Tricep Extension', 'Leg Press',
            'Lunges', 'Lateral Raise', 'Face Pull', 'Cable Fly', 'Leg Curl'
        ]
        
        for _ in range(count):
            coach = random.choice(coaches)
            user = random.choice(users)
            start_date = fake.date_between(start_date='-60d', end_date='today')
            end_date = fake.date_between(start_date=start_date, end_date='+90d')
            
            plan = TrainingPlan.objects.create(
                coach=coach,
                user=user,
                name=f"{fake.word().title()} Training Plan",
                description=fake.text(max_nb_chars=250),
                start_date=start_date,
                end_date=end_date,
                is_active=random.choice([True, False])
            )
            
            # Add 5-10 exercises to the plan
            for order in range(random.randint(5, 10)):
                # Use day_of_week for some, scheduled_date for others
                # Avoid day_of_week=0 due to model validation bug (0 is falsy)
                use_day_of_week = random.choice([True, False])
                if use_day_of_week:
                    day_of_week = random.randint(1, 6)
                    scheduled_date = None
                else:
                    day_of_week = None
                    scheduled_date = fake.date_between(start_date=start_date, end_date=end_date)
                
                TrainingPlanExercise.objects.create(
                    plan=plan,
                    exercise_name=random.choice(exercise_names),
                    day_of_week=day_of_week,
                    scheduled_date=scheduled_date,
                    sets=random.randint(2, 5),
                    reps=random.randint(6, 15),
                    weight_kg=Decimal(str(round(random.uniform(10, 150), 2))),
                    rest_seconds=random.choice([30, 60, 90, 120]),
                    order=order,
                    notes=fake.sentence() if random.random() > 0.7 else None
                )

    def generate_meals(self, users, count):
        """Generate meals with food items."""
        meal_types = ['breakfast', 'lunch', 'dinner', 'snack', 'pre_workout', 'post_workout']
        food_names = [
            'Chicken Breast', 'Brown Rice', 'Broccoli', 'Salmon', 'Sweet Potato',
            'Eggs', 'Oatmeal', 'Banana', 'Protein Shake', 'Greek Yogurt',
            'Almonds', 'Avocado', 'Quinoa', 'Spinach', 'Tuna', 'Pasta',
            'Turkey', 'Cottage Cheese', 'Berries', 'Olive Oil'
        ]
        
        for _ in range(count):
            user = random.choice(users)
            date = fake.date_between(start_date='-30d', end_date='today')
            
            meal = Meal.objects.create(
                user=user,
                name=fake.sentence(nb_words=3),
                meal_type=random.choice(meal_types),
                date=date,
                time=fake.time_object(),
                calories=random.randint(200, 800),
                protein_g=Decimal(str(round(random.uniform(10, 60), 2))),
                carbs_g=Decimal(str(round(random.uniform(20, 100), 2))),
                fat_g=Decimal(str(round(random.uniform(5, 40), 2))),
                notes=fake.text(max_nb_chars=150) if random.random() > 0.5 else None
            )
            
            # Add 2-5 food items per meal
            for _ in range(random.randint(2, 5)):
                Food.objects.create(
                    meal=meal,
                    name=random.choice(food_names),
                    quantity=f"{random.randint(50, 300)}g",
                    calories=random.randint(50, 300),
                    protein_g=Decimal(str(round(random.uniform(2, 30), 2))),
                    carbs_g=Decimal(str(round(random.uniform(5, 50), 2))),
                    fat_g=Decimal(str(round(random.uniform(1, 20), 2)))
                )

    def generate_nutrition_plans(self, coaches, users, count):
        """Generate nutrition plans with meals."""
        meal_types = ['breakfast', 'lunch', 'dinner', 'snack', 'pre_workout', 'post_workout']
        
        for _ in range(count):
            coach = random.choice(coaches)
            user = random.choice(users)
            start_date = fake.date_between(start_date='-60d', end_date='today')
            end_date = fake.date_between(start_date=start_date, end_date='+90d')
            
            plan = NutritionPlan.objects.create(
                coach=coach,
                user=user,
                name=f"{fake.word().title()} Nutrition Plan",
                description=fake.text(max_nb_chars=250),
                target_calories=random.randint(1500, 3500),
                target_protein_g=Decimal(str(round(random.uniform(100, 250), 2))),
                target_carbs_g=Decimal(str(round(random.uniform(150, 400), 2))),
                target_fat_g=Decimal(str(round(random.uniform(40, 120), 2))),
                start_date=start_date,
                end_date=end_date,
                is_active=random.choice([True, False])
            )
            
            # Add 4-6 meal timings to the plan
            for order, meal_type in enumerate(random.sample(meal_types, random.randint(4, 6))):
                hour = random.randint(6, 22)
                minute = random.choice([0, 15, 30, 45])
                
                NutritionPlanMeal.objects.create(
                    plan=plan,
                    meal_type=meal_type,
                    scheduled_time=time(hour=hour, minute=minute),
                    target_calories=random.randint(200, 800),
                    target_protein_g=Decimal(str(round(random.uniform(10, 60), 2))),
                    target_carbs_g=Decimal(str(round(random.uniform(20, 100), 2))),
                    target_fat_g=Decimal(str(round(random.uniform(5, 40), 2))),
                    is_pre_workout=(meal_type == 'pre_workout'),
                    is_post_workout=(meal_type == 'post_workout'),
                    notes=fake.text(max_nb_chars=150) if random.random() > 0.5 else None,
                    order=order
                )

    def generate_checkins(self, users, count):
        """Generate check-ins."""
        moods = ['excellent', 'good', 'neutral', 'poor', 'bad']
        
        for _ in range(count):
            user = random.choice(users)
            date = fake.date_between(start_date='-30d', end_date='today')
            
            # Avoid duplicate check-ins for the same user on the same date
            if CheckIn.objects.filter(user=user, date=date).exists():
                continue
            
            CheckIn.objects.create(
                user=user,
                date=date,
                weight_kg=Decimal(str(round(random.uniform(50, 120), 2))),
                body_fat_percentage=Decimal(str(round(random.uniform(8, 35), 1))),
                muscle_mass_kg=Decimal(str(round(random.uniform(30, 80), 2))),
                mood=random.choice(moods),
                energy_level=random.randint(1, 10),
                sleep_hours=Decimal(str(round(random.uniform(4, 10), 1))),
                water_intake_ml=random.randint(500, 4000),
                notes=fake.text(max_nb_chars=150) if random.random() > 0.5 else None
            )

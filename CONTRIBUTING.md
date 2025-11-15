# Contributing to The Circus Grove

Thank you for considering contributing to The Circus Grove! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Screenshots if applicable
- Your environment (OS, browser, versions)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Include:

- A clear, descriptive title
- Detailed description of the proposed feature
- Rationale for why this enhancement would be useful
- Any relevant examples or mockups

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Follow the coding standards** outlined below
3. **Write clear commit messages** following conventional commits
4. **Add tests** for new features
5. **Update documentation** as needed
6. **Ensure all tests pass** before submitting
7. **Submit the pull request** with a clear description

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/the_circus_grove.git
cd the_circus_grove

# Setup the project
make setup

# Create a new branch
git checkout -b feature/your-feature-name
```

## Coding Standards

### Python (Backend)

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Maximum line length: 88 characters (Black formatter)
- Write docstrings for all public methods and classes
- Use type hints where appropriate

```python
# Good
def create_training_session(
    user: User, 
    title: str, 
    date: datetime.date
) -> TrainingSession:
    """Create a new training session.
    
    Args:
        user: The user creating the session
        title: Session title
        date: Session date
        
    Returns:
        TrainingSession: The created session
    """
    return TrainingSession.objects.create(
        user=user,
        title=title,
        date=date
    )
```

### JavaScript/Vue (Frontend)

- Use ES6+ syntax
- Follow Vue 3 Composition API conventions
- Use meaningful variable and function names
- Prefer const over let, avoid var
- Use async/await over promises
- Add JSDoc comments for complex functions

```javascript
// Good
const fetchTrainingSessions = async () => {
  loading.value = true
  try {
    const response = await trainingApi.getSessions()
    sessions.value = response.data.results
  } catch (error) {
    console.error('Failed to fetch sessions:', error)
    showError('Failed to load training sessions')
  } finally {
    loading.value = false
  }
}
```

### Vue Components

- Use Composition API with `<script setup>`
- Keep components focused and single-purpose
- Extract reusable logic into composables
- Use props and emits for component communication
- Follow mobile-first responsive design

```vue
<template>
  <div class="container mx-auto px-4">
    <!-- Mobile-first design -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  title: String,
  required: true
})

const emit = defineEmits(['save', 'cancel'])
</script>
```

## Commit Message Guidelines

Use conventional commits format:

```
type(scope): subject

body

footer
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```bash
feat(training): add exercise library component
fix(auth): resolve token refresh race condition
docs(api): update authentication endpoint docs
refactor(nutrition): extract meal form into component
```

## Testing

### Backend Tests

```bash
# Run all tests
make test

# Run specific app tests
docker compose exec backend python manage.py test users

# Run with coverage
docker compose exec backend coverage run --source='.' manage.py test
docker compose exec backend coverage report
```

### Frontend Tests

```bash
# Run tests (when implemented)
cd frontend
npm run test

# Run with coverage
npm run test:coverage
```

## Documentation

- Update README.md for user-facing changes
- Update API.md for API changes
- Update DEVELOPMENT.md for development process changes
- Add inline comments for complex logic
- Keep documentation up-to-date with code changes

## Review Process

1. **Self-review**: Review your own code before submitting
2. **CI checks**: Ensure all automated checks pass
3. **Code review**: Address reviewer feedback promptly
4. **Testing**: Verify changes work as expected
5. **Merge**: Maintainer will merge when approved

## Project Structure

```
the_circus_grove/
├── backend/
│   ├── users/           # User management
│   ├── training/        # Training sessions
│   ├── nutrition/       # Nutrition tracking
│   └── checkins/        # Daily check-ins
├── frontend/
│   ├── src/
│   │   ├── api/        # API client
│   │   ├── stores/     # Pinia stores
│   │   ├── router/     # Routes
│   │   └── views/      # Page components
└── docs/               # Documentation
```

## Release Process

1. Version bump in package files
2. Update CHANGELOG.md
3. Create release notes
4. Tag the release
5. Deploy to production

## Getting Help

- Check documentation in `/docs`
- Review existing issues
- Ask questions in discussions
- Contact maintainers

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project website (when available)

Thank you for contributing to The Circus Grove! 🎪

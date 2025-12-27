# Deployment Guide for Udaipur Local Guide AI

This guide explains how to deploy the Udaipur Local Guide AI web application using various platforms.

## Quick Start - Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy your app for free:

### Prerequisites
- GitHub account
- Repository pushed to GitHub with all project files

### Steps
1. **Visit Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io)
2. **Sign in**: Use your GitHub account
3. **New App**: Click "New app"
4. **Repository**: Select your GitHub repository
5. **Main File**: Set `streamlit_app.py` as the main file path
6. **Deploy**: Click "Deploy" and wait for the build to complete

Your app will be live at: `https://[your-app-name].streamlit.app`

## Local Development

### Run Streamlit Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

### Run Command Line Version
```bash
python app.py
```

## Alternative Deployment Platforms

### Heroku Deployment

1. **Create Procfile**:
```bash
echo "web: streamlit run streamlit_app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
```

2. **Deploy to Heroku**:
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```

### Railway Deployment

1. **Connect Repository**: Link your GitHub repo to Railway
2. **Configure**: Set `streamlit run streamlit_app.py` as the start command
3. **Deploy**: Railway will automatically deploy

### Render Deployment

1. **Create Web Service**: Connect your GitHub repository
2. **Build Command**: `pip install -r requirements.txt`
3. **Start Command**: `streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`

## Environment Configuration

### Required Files
- `streamlit_app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `.streamlit/config.toml` - Streamlit configuration
- `packages.txt` - System dependencies (if needed)
- `.kiro/product.md` - Local knowledge context file

### Environment Variables
No environment variables are required. The app uses local file-based context.

## Troubleshooting

### Common Issues

**Import Errors**:
- Ensure all files are in the repository
- Check that `src/` directory and all Python files are included

**Context File Missing**:
- Verify `.kiro/product.md` exists in the repository
- Check file permissions and encoding

**Streamlit Configuration**:
- Ensure `.streamlit/config.toml` is properly formatted
- Check theme colors are valid hex codes

### Performance Optimization

**For Production**:
- Enable caching in Streamlit using `@st.cache_data`
- Optimize context loading for faster startup
- Consider using session state for better user experience

## Security Considerations

- The app doesn't require authentication
- No sensitive data is stored or transmitted
- All responses are based on local context file
- Consider rate limiting for public deployments

## Monitoring and Maintenance

### Logs
- Streamlit Cloud provides built-in logging
- Check deployment logs for errors
- Monitor app performance and usage

### Updates
- Push changes to GitHub to trigger automatic redeployment
- Test locally before deploying
- Keep dependencies updated in `requirements.txt`

## Support

For deployment issues:
- Check Streamlit Cloud documentation
- Review platform-specific deployment guides
- Ensure all required files are in the repository
- Test the app locally first
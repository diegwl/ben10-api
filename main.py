if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run('port.fastapi.app:core_module', host='0.0.0.0', port=8000, log_level="info", reload=True)
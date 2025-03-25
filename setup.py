from setuptools import setup, find_packages

setup(
    name="models_pack",  # Nombre del paquete
    version="0.1.0",
    description="Modelos para predicción de precios de vuelos",
    author="Cristian",
    packages=find_packages(),  # Encuentra paquetes en el proyecto
    package_data={
        "": ["model/*.keras", "model/*.pkl"]  # ✅ Incluye archivos en `model/`
    },
    include_package_data=True,
    install_requires=[
        "Flask",
        "pandas",
        "numpy",
        "tensorflow",
        "joblib",
        "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
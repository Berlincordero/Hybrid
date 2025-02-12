# utils.py
import subprocess
import os

def optimize_video(video_instance):
    """
    Optimiza el archivo de video para que el 'moov atom' se encuentre al inicio.
    """
    # Ruta del archivo original
    input_path = video_instance.video_file.path
    # Ruta temporal para el archivo optimizado
    optimized_path = os.path.join(os.path.dirname(input_path), "optimized_" + os.path.basename(input_path))
    
    # Comando para ejecutar ffmpeg y mover el 'moov atom' al inicio
    command = [
        "ffmpeg",
        "-i", input_path,
        "-c", "copy",
        "-movflags", "faststart",
        optimized_path
    ]
    
    # Ejecuta el comando; si falla, se lanzará una excepción
    subprocess.run(command, check=True)
    
    # Reemplaza el archivo original por el optimizado
    os.replace(optimized_path, input_path)

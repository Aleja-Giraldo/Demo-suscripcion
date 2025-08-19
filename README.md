
# Demo: Chat de 1 página (Streamlit)

App mínima para mostrar la experiencia de un modelo en una sola página.

## Ejecutar en local
1. Crea y activa un entorno:
   ```bash
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Define tu API key de OpenAI como variable de entorno:
   - macOS/Linux:
     ```bash
     export OPENAI_API_KEY="tu_clave"
     ```
   - Windows (PowerShell):
     ```powershell
     setx OPENAI_API_KEY "tu_clave"
     $env:OPENAI_API_KEY="tu_clave"
     ```
3. Ejecuta la app:
   ```bash
   streamlit run app.py
   ```

## Desplegar en Streamlit Community Cloud
1. Sube este folder a un repositorio en GitHub.
2. Ve a https://share.streamlit.io → "New app" → conecta tu repo.
3. En **Settings → Secrets**, agrega:
   ```
   OPENAI_API_KEY = "tu_clave"
   ```
4. Guarda y lanza la app. Obtendrás un link público.

## Personalizaciones
- Cambia el modelo en `app.py` (línea con `model="gpt-4o-mini"`).
- Ajusta el tono con `temperature`.
- Agrega un mensaje de sistema (p. ej. guías de estilo) insertando al inicio del historial:
  ```python
  system_msg = {"role":"system","content":"Eres un asistente conciso y profesional."}
  messages=[system_msg]+messages
  ```

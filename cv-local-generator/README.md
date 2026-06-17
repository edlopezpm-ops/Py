# CV Local Generator

App local para editar datos de un CV, importar/exportar JSON y generar un documento Word-compatible o PDF desde el navegador.

## Objetivo del proyecto

La idea es tener un flujo simple:

1. Tu AI lee tu CV base y la descripcion del cargo.
2. La AI devuelve un JSON con textos adaptados para ese cargo.
3. Pegas o importas ese JSON en esta app.
4. Revisas y ajustas los textos.
5. Generas el CV final en Word-compatible o PDF.

## Como abrir la app

Abre este archivo en tu navegador:

`app.html`

No necesitas instalar nada para esta primera version.

## Archivos importantes

- `app.html`: toda la app local: estructura, estilos y JavaScript.
- `data/sample-cv.json`: ejemplo de datos que la app puede importar.
- `docs/ai-json-prompt.md`: prompt guia para pedirle a una AI que genere JSON compatible.

## Formato JSON esperado

```json
{
  "profile": {
    "name": "Tu Nombre",
    "title": "Cargo objetivo",
    "location": "Ciudad, Pais",
    "phone": "+1 000 000 0000",
    "email": "correo@email.com",
    "linkedin": "linkedin.com/in/usuario",
    "summary": "Resumen profesional..."
  },
  "skills": ["Skill 1", "Skill 2"],
  "experience": [
    {
      "role": "Cargo",
      "company": "Empresa",
      "period": "2022 - Presente",
      "bullets": ["Logro 1", "Logro 2"]
    }
  ],
  "education": [
    {
      "degree": "Titulo",
      "institution": "Institucion",
      "period": "2018 - 2022"
    }
  ]
}
```

## Siguiente etapa recomendada

Cuando esta version te quede clara, el siguiente paso es separar el proyecto en:

- `index.html`
- `styles.css`
- `app.js`

Despues podemos crear una version Python con generacion real de `.docx` y `.pdf`.

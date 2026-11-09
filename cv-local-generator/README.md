# CV Local Generator

App local para evaluar cargos contra un CV master, adaptar un CV segun palabras clave, y generar CV + cover letter en PDF.

## Objetivo del proyecto

La idea es tener un flujo simple:

1. Guardas tus documentos master en `core/`.
2. Pegas una descripcion de cargo o guardas archivos en `jobs/`.
3. La app compara el cargo contra el core CV y core experience.
4. Recibes un indicador heurístico de coincidencia de palabras clave para revisar la candidatura.
5. Decides si procede generar el paquete.
6. La app genera CV + cover letter en PDF.

<!-- (kommiBo) Distinguish keyword scoring and fixed templates from verified career facts. -->
`assess_fit` calcula coincidencia de palabras clave y limita el score al rango 8–96;
ese número no es una probabilidad calibrada de contratación ni una garantía de resultado.
Los textos de la UI que hablan de probabilidad deben interpretarse con ese límite.

`adapt_cv` reordena contenido, infiere un título y construye un resumen. La cover letter
incluye frases de plantilla sobre experiencia empresarial que pueden no corresponder a
otro candidato. Revisa cada afirmación, empresa, fecha y logro antes de enviar un PDF;
la generación local no verifica su veracidad. Consulta los [límites de uso](../TERMS.md).

## Documentos master

Los archivos master viven en:

```text
core/core-cv.txt
core/core-experience.txt
```

Para cambiar la experiencia base, reemplaza esos archivos con nuevos documentos usando los mismos nombres. Luego reinicia o refresca la app.

`core-cv.txt` debe contener el CV master limpio.

`core-experience.txt` puede contener notas largas, historia profesional, detalles tecnicos, aprendizajes y contexto que ayuden a redactar mejor el CV y la cover letter.

## Version Python recomendada

<!-- (kommiBo) Make the working directory and launcher effects explicit. -->
Para instalar las dependencias manualmente desde la carpeta raiz `Py`:

```powershell
py -m pip install -r .\cv-local-generator\requirements.txt
```

Desde la carpeta raiz `Py`, puedes ejecutar la app de escritorio con un solo comando:

```powershell
.\Run-CVGenerator.ps1
```

Si estas dentro de `cv-local-generator`, usa:

```powershell
.\Run-CVGenerator.ps1
```

Para ejecutar la comprobacion funcional sin abrir la ventana:

```powershell
.\Run-CVGenerator.ps1 -Check
```

Ambos launchers instalan las dependencias si falta `reportlab`. Ademas, `-Check`
compila los modulos, lee los documentos de `core/` y `jobs/sample-job.txt`, y genera
un CV y una cover letter en `output/pdf/` dentro de `cv-local-generator`. No es una
comprobacion de solo lectura: usa una copia con datos sinteticos si no quieres
generar documentos con los masters actuales.

Para abrir la version navegador:

```powershell
.\Run-CVGenerator.ps1 -Web
```

Tambien puedes ejecutar la app web directamente desde `cv-local-generator`:

```powershell
py cv_app.py
```

Abre en el navegador:

```text
http://127.0.0.1:8765
```

## Version escritorio

Tambien puedes usar una UI simple de escritorio desde `cv-local-generator`:

```powershell
py desktop_app.py
```

La ventana guia el flujo:

1. Confirmar los archivos master en `core/`.
2. Cargar o pegar la descripcion del cargo.
3. Evaluar el cargo.
4. Generar CV + cover letter.
5. Abrir `output/pdf/`.

Los PDFs se guardan en:

```text
output/pdf/
```

## Flujo con AI sin API paga

La app incluye un prompt listo para copiar en ChatGPT manualmente. Esto permite que una persona use una cuenta ChatGPT Free como apoyo, sin integrar llamadas automaticas a la API.

<!-- (kommiBo) Local operation is separate from licensing and external assistant costs. -->
La versión actual funciona localmente y no integra una API de modelos ni facturación por
tokens. Si copias el prompt a otro asistente, sus condiciones y límites se evalúan por
separado; no se presupone acceso gratuito, una cuenta concreta ni autorización para enviar
datos personales. El proyecto no tiene una licencia general seleccionada: consulta el
[inventario de licencias](../docs/licensing.md) antes de redistribuirlo.

## Crear instalador / EXE para Windows

Desde `cv-local-generator`, crea una carpeta distribuible con un `.exe`:

```powershell
.\build_windows_exe.ps1
```

El resultado queda en:

```text
dist/CVLocalGenerator/CVLocalGenerator.exe
```

<!-- (kommiBo) The distribution can contain personal source documents. -->
El build copia `core/`, `jobs/`, `data/` y `docs/` a la carpeta distribuible tal como están;
no anonimiza sus contenidos. Antes de compilar y compartir, prepara una copia con datos
sintéticos o cuya divulgación esté autorizada y revisa todo el paquete final.

Si cuentas con los permisos necesarios para distribuirlo, entrega la carpeta completa
`dist/CVLocalGenerator`, no sólo el `.exe`. El build crea `output/pdf/`; los PDFs generados
al usar la app son datos locales que también debes revisar antes de compartir esa carpeta.
Consulta la [guía de manejo de datos](../docs/data-handling.md).

Para una experiencia tipo instalador, puedes comprimir esa carpeta en `.zip`. Mas adelante se puede agregar Inno Setup o WiX para generar un instalador `.msi` o `.exe` con accesos directos.

## Cargos soportados

Coloca descripciones de cargo en `jobs/` con estos formatos:

- `.txt`
- `.md`
- `.csv`
- `.html`
- `.htm`
- `.docx`

Los archivos `.doc` antiguos no se leen sin Microsoft Word. Guardalos como `.docx` o `.txt`.

## Version HTML simple

Abre este archivo en tu navegador:

`app.html`

No necesitas instalar nada para esa version, pero el PDF se hace desde la ventana de impresion del navegador.

## Archivos importantes

- `app.html`: toda la app local: estructura, estilos y JavaScript.
- `cv_app.py`: app Python local con lectura de cargos, adaptacion por keywords y PDF real.
- `desktop_app.py`: UI de escritorio con pasos guiados.
- `build_windows_exe.ps1`: build de Windows con PyInstaller.
- `core/core-cv.txt`: CV master usado como base.
- `core/core-experience.txt`: experiencia master usada para assessment y cover letter.
- `data/sample-cv.json`: ejemplo de datos que la app puede importar.
- `jobs/sample-job.txt`: ejemplo de cargo para probar la adaptacion.
- `docs/ai-json-prompt.md`: prompt guia para pedirle a una AI que genere JSON compatible.

## Formato JSON esperado

<!-- (kommiBo) Separate editable preview state from the Python web export input. -->
En la version web Python, editar el JSON actualiza solo la vista previa. El boton
`Generar CV + Cover Letter` envia unicamente la descripcion del cargo y reconstruye
el paquete desde los archivos master: las ediciones del JSON no pasan a los PDFs
y la respuesta reemplaza la vista previa. Revisa los documentos generados antes
de usarlos; una correccion visible en el preview no acredita una correccion en el PDF.

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

<!-- (kommiBo) Local processing, disclosure and paid-API boundaries. -->
Cualquier futura asistencia de AI requiere una decisión separada de alcance, privacidad y costo; no se habilitan APIs pagadas por defecto. Revisa el prompt antes de copiar datos personales a otra herramienta. Los PDFs, archivos core y jobs permanecen en disco hasta que los elimines; consulta la [guía de manejo de datos](../docs/data-handling.md).

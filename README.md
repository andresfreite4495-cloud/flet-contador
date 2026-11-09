# Contador interactivo con Flet

**Biblioteca:** [Flet](https://flet.dev) (Python)
**Autor:** _(escribe aquí tu nombre)_

Aplicación mínima que muestra un contador en pantalla. Cada vez que el usuario presiona el botón **Sumar +1**, el número aumenta; el botón **Reiniciar** lo devuelve a cero. Está escrita con programación orientada a objetos (reto adicional).

![Captura de la aplicación funcionando](capturas/captura.png)

---

## 1. Instalación y ejecución

Requisitos: **Python 3.10 o superior** (según la documentación oficial de Flet).

```bash
# 1. Clonar el repositorio
git clone <URL-de-tu-repositorio>
cd flet-contador

# 2. Crear y activar un entorno virtual
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
flet run main.py
```

También se puede ejecutar con `python main.py`, aunque la documentación recomienda `flet run`. Para verla en el navegador: `flet run --web main.py`.

Para comprobar la instalación: `flet --version` o `flet doctor`.

---

## 2. Investigación

### ¿Qué es Flet y cuál es su propósito?
Flet es un framework para construir interfaces de usuario interactivas en Python sin necesidad de conocer HTML, CSS o JavaScript. Su interfaz se arma con *controles* basados en widgets de [Flutter](https://flutter.dev/), lo que le da un aspecto moderno y consistente. Su propósito es permitir que un programador de Python cree aplicaciones gráficas completas usando solo Python.

### ¿Qué tipo de aplicaciones permite desarrollar?
Aplicaciones de **escritorio** (Windows, macOS, Linux), **web** y **móviles** (iOS y Android) con el mismo código. Un mismo programa puede ejecutarse en una ventana nativa o en el navegador.

### ¿Cómo se instala y qué requisitos tiene?
- Python 3.10 o superior.
- Sistemas operativos soportados según la documentación: Windows 10/11 de 64 bits, macOS 12 o superior, y Debian/Ubuntu en Linux.
- Instalación: `pip install flet` (la documentación también muestra `pip install 'flet[all]'`).
- Se recomienda usar un entorno virtual.

### ¿Cuáles son sus principales componentes gráficos?
Todo en Flet es un **control**. Algunos de los más usados:
- `Text`: muestra texto.
- `Button`, `IconButton`, `TextButton`: botones.
- `TextField`, `Checkbox`, `Dropdown`: formularios y entrada de datos.
- `Row`, `Column`, `Stack`: contenedores que organizan a otros controles.
- `Page`: la ventana o página principal donde se agregan los controles.

### ¿Cómo maneja los eventos del usuario?
Cada control tiene propiedades de evento, como `on_click` (botones) o `on_change` (campos de texto, casillas). A esa propiedad se le asigna una **función** que Flet llama automáticamente cuando el usuario interactúa; la función recibe un objeto de evento `e`. Dentro del manejador se modifican las propiedades de los controles (por ejemplo `texto.value = "..."`) y se llama a `page.update()` (o `self.update()` en un control personalizado) para enviar los cambios a la pantalla.

### Ventajas y limitaciones frente a Tkinter
_(Esta comparación es análisis propio a partir de la documentación consultada y del uso habitual de ambas bibliotecas.)_

| | Flet | Tkinter |
|---|---|---|
| Instalación | Requiere `pip install flet` | Viene incluida con Python |
| Plataformas | Escritorio, web y móvil | Solo escritorio |
| Aspecto visual | Moderno (basado en Flutter) | Más clásico/básico |
| Componentes | Más de 100 controles integrados | Conjunto más pequeño de widgets |
| Madurez y comunidad | Más reciente, la API ha cambiado entre versiones | Muy estable, mucha documentación |
| Peso | Descarga e instala un cliente gráfico adicional | Ligero |

**Ventaja principal:** una sola base de código para escritorio, web y móvil con un aspecto moderno.
**Limitaciones:** es una dependencia externa más pesada y, al ser más joven, su API ha cambiado entre versiones (ejemplos antiguos con `ft.app(...)` o `UserControl` pueden no funcionar igual en versiones nuevas).

---

## 3. Explicación del funcionamiento del ejemplo

El archivo `main.py` tiene tres clases/funciones:

| Elemento | Responsabilidad |
|---|---|
| `ContadorModelo` (clase) | Guarda el valor del contador y tiene la lógica (`incrementar`, `reiniciar`). No sabe nada de la interfaz. |
| `ContadorVista` (clase, hereda de `ft.Column`) | Construye los componentes visuales, detecta los clics y actualiza lo que se ve en pantalla. |
| `main(page)` (función) | Configura la ventana principal y agrega la vista. |

1. **Cómo se crea la ventana principal:** `ft.run(main)` inicia la aplicación y Flet le pasa a `main` un objeto `page`, que representa la ventana. Allí se define el título (`page.title`) y la alineación.
2. **Cómo se crean y muestran los componentes:** dentro de `ContadorVista.init()` se crean un `ft.Text` (el número) y dos `ft.Button`. Se organizan con `ft.Column` y `ft.Row`, y se muestran con `page.add(ContadorVista())`.
3. **Qué evento se implementó y cómo se detecta:** el evento de **clic** (`on_click`). Se detecta al asignar `on_click=self.al_hacer_clic_sumar` al botón: Flet queda escuchando el clic y llama a ese método cuando ocurre.
4. **Qué función responde al evento:** `al_hacer_clic_sumar` (y `al_hacer_clic_reiniciar` para el otro botón). Estos métodos llaman al modelo (`self.modelo.incrementar()`) y luego a `actualizar_texto()`.
5. **Cómo se modifica la interfaz:** `actualizar_texto()` cambia `self.texto.value` por el nuevo número y llama a `self.update()`, que envía el cambio a la pantalla. Así el usuario ve el contador subir.

---

## Fuentes consultadas

- Flet, *Installation*: https://flet.dev/docs/getting-started/installation
- Flet, *Installation* (documentación): https://docs.flet.dev/getting-started/installation
- Flet, *Controls* (eventos y `page.update()`): https://flet.dev/docs/archive/flet-controls
- Flet, *Custom Controls* (POO: controles estilizados y compuestos, `@ft.control`): https://flet.dev/docs/cookbook/custom-controls
- Flet, *User controls* (enfoque antiguo con `UserControl`): https://flet.dev/docs/guides/python/user-controls
- Sitio oficial: https://flet.dev

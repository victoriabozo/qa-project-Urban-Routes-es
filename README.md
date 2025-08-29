# Automatización Urban Routes - Sprint 8
Este proyecto, realizado como parte del bootcamp de QA de TripleTen, automatiza la validación del flujo completo de reserva de un taxi dentro de la aplicación *Urban Routes*, conforme a los requisitos funcionales establecidos para el Sprint 8. Las pruebas simulan interacciones reales del usuario, desde la selección de la ruta hasta la confirmación del pedido, e incluye configuraciones adicionales.

## Tecnologías y técnicas utilizadas
- Python como lenguaje.
- Selenium WebDriver para automatización de interfaz gráfica (UI).
- pytest como framework de pruebas.
- Page Object Model (POM) para estructuración y mantenimiento del código.
- Google Chrome como navegador. 
- Técnicas de localización por XPATH, CSS Selectors, ID y Class Name.
- WebDriverWait y Expected Conditions para sincronización controlada.
- Aserciones para validar inputs, visualización de elementos, y estados activos de componentes.

## Instrucciones para ejecutar las pruebas
- Clona el repositorio en tu entorno local con SSH. Reemplaza “username” con tu nombre de usuario:
     ```sh
   git clone git@github.com:username/qa-project-Urban-Routes-es.git
   ```
- Instala pytest para ejecutar las pruebas:
    ```sh
  pip install pytest
   ```
- Ejecuta todas las pruebas con pytest:
    ```sh
  pytest
   ```

## Estructura de las pruebas automatizadas
- Configurar dirección de origen y destino.
- Seleccionar la tarifa Comfort.
- Ingresar y confirmar número de teléfono.
- Agregar una tarjeta de crédito.
- Escribir un mensaje para el conductor.
- Solicitar manta y pañuelos.
- Agregar dos (2) helados al pedido.
- Confirmar visualización del modal de estado del pedido.

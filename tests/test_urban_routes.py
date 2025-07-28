from data import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import urban_routes_page as urp
from utils import retrieve_code


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)

# 1. Configurar la dirección:
    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

# 2. Seleccionar la tarifa Comfort:
    def test_select_comfort_rate(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_rate_icon()
        assert self.routes_page.is_comfort_rate_selected()

# 3. Rellenar el número de teléfono:
    def test_set_phone_number(self):
        phone = data.phone_number
        self.routes_page.click_phone_number_button()
        self.routes_page.set_phone_number(phone)
        self.routes_page.click_phone_form_next_button()
        code = retrieve_code.retrieve_phone_code(self.driver)
        self.routes_page.set_confirmation_code(code)
        self.routes_page.click_confirm_code_button()
        assert self.routes_page.get_phone_number() == phone

# 4. Agregar una tarjeta de crédito:
    def test_add_credit_card(self):
        number_of_card = data.card_number
        code_of_card = data.card_code
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number_field(number_of_card)
        self.routes_page.set_card_code_field(code_of_card)
        self.routes_page.set_click_outside_to_activate()
        self.routes_page.click_add_card_details_button()
        self.routes_page.click_close_card_section_button()
        assert self.routes_page.is_card_added()

# 5. Escribir un mensaje para el controlador:
    def test_write_message_for_driver(self):
        message_driver = data.message_for_driver
        self.routes_page.set_message_for_driver_field(message_driver)
        assert self.routes_page.get_message_for_driver() == message_driver

# 6. Pedir una manta y pañuelos:
    def test_add_blanket_and_tissues(self):
        self.routes_page.click_blanket_tissues_slider()
        assert self.routes_page.is_blanket_tissues_selected()

# 7. Pedir 2 helados:
    def test_add_ice_cream(self):
        self.routes_page.click_ice_cream_counter_plus()
        self.routes_page.click_ice_cream_counter_plus()
        count = self.routes_page.get_ice_cream_count()
        assert count == 2

# 8. Aparece el modal para buscar un taxi:
    def test_is_order_progress_modal_active(self):
        detail_of_order = self.routes_page.get_order_progress_details()
        self.routes_page.click_request_taxi_now_button()
        assert detail_of_order.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
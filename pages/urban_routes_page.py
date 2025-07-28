from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    request_taxi_button = (By.CSS_SELECTOR, ".button.round")
    comfort_rate = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']/..")
    phone_number_button = (By.CSS_SELECTOR, ".np-button")
    phone_number_field = (By.ID, "phone")
    phone_form_next_button = (By.XPATH, "//button[@type='submit' and contains(@class, 'full') and text()='Siguiente']")
    confirm_code_field = (By.CSS_SELECTOR, ".input-container #code")
    confirm_code_button = (By.CSS_SELECTOR, "div.section.active form div.buttons > button.button.full[type='submit']")
    payment_method_button = (By.CSS_SELECTOR, "div.pp-button.filled")
    add_card_button = (By.CSS_SELECTOR, "div.pp-row.disabled")
    card_number_field = (By.ID, "number")
    card_code_field = (By.CSS_SELECTOR, "input.card-input#code")
    click_out_to_activate_add_card_details_button = (By.CSS_SELECTOR, ".plc")
    add_card_details_button = (By.XPATH, "//button[text()='Agregar']")
    close_card_section_button = (By.CSS_SELECTOR, "div.payment-picker.open div.section.active > button.close-button.section-close")
    card_image = (By.CSS_SELECTOR, 'div.pp-button.filled img[alt="card"]')
    message_for_driver_field =  (By.ID, "comment")
    blanket_tissues_slider = (By.CSS_SELECTOR, "div.r-sw-container div.r-sw div.switch > span.slider.round")
    blanket_tissues_checkbox = (By.CSS_SELECTOR, "div.r-sw-container div.r-sw div.switch > input.switch-input")
    ice_cream_counter_plus = (By.XPATH, "//div[contains(@class,'r-counter-container') and .//div[contains(text(),'Helado')]]//div[contains(@class,'counter-plus')]")
    ice_cream_counter = (By.XPATH, "//div[contains(text(),'Helado')]/ancestor::div[contains(@class,'r-counter-container')]//div[contains(@class,'counter-value')]")
    request_taxi_now_button = (By.CLASS_NAME, "smart-button-secondary")
    order_progress_details = (By.CSS_SELECTOR, "div.order-body")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

# 1. Configurar la dirección:
    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)
    def set_to(self, to_address):
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

# 2. Seleccionar la tarifa Comfort:
    def get_request_taxi_button(self):
        return self.wait.until(EC.presence_of_element_located(self.request_taxi_button))
    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()
    def get_comfort_rate_icon(self):
        return self.wait.until(EC.presence_of_element_located(self.comfort_rate))
    def click_comfort_rate_icon(self):
        self.get_comfort_rate_icon().click()
    def is_comfort_rate_selected(self):
        comfort_icon = self.get_comfort_rate_icon()
        return "active" in comfort_icon.get_attribute("class")

# 3. Rellenar el número de teléfono:
    def get_phone_number_button(self):
        return self.wait.until(EC.presence_of_element_located(self.phone_number_button))
    def click_phone_number_button(self):
        self.get_phone_number_button().click()
    def set_phone_number(self, phone):
        self.wait.until(EC.presence_of_element_located(self.phone_number_field)).send_keys(phone)
    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')
    def get_phone_form_next_button(self):
        return self.wait.until(EC.presence_of_element_located(self.phone_form_next_button))
    def click_phone_form_next_button(self):
        self.get_phone_form_next_button().click()
    def set_confirmation_code(self, code):
        self.wait.until(EC.presence_of_element_located(self.confirm_code_field)).send_keys(code)
    def get_confirm_code_button(self):
        return self.wait.until(EC.presence_of_element_located(self.confirm_code_button))
    def click_confirm_code_button(self):
        self.get_confirm_code_button().click()

# 4. Agregar una tarjeta de crédito:
    def get_payment_method_button(self):
        return self.wait.until(EC.presence_of_element_located(self.payment_method_button))
    def click_payment_method_button(self):
        self.get_payment_method_button().click()
    def get_add_card_button(self):
        return self.wait.until(EC.presence_of_element_located(self.add_card_button))
    def click_add_card_button(self):
        self.get_add_card_button().click()
    def get_card_number_field(self):
        return self.wait.until(EC.presence_of_element_located(self.card_number_field))
    def set_card_number_field(self, card_number):
        self.get_card_number_field().send_keys(card_number)
    def get_card_code_field(self):
        return self.wait.until(EC.presence_of_element_located(self.card_code_field))
    def set_card_code_field(self, card_code):
        self.get_card_code_field().send_keys(card_code)
    def set_click_outside_to_activate(self):
        return self.wait.until(EC.presence_of_element_located(self.click_out_to_activate_add_card_details_button)).click()
    def get_add_card_details_button(self):
        return self.wait.until(EC.presence_of_element_located(self.add_card_details_button))
    def click_add_card_details_button(self):
        self.get_add_card_details_button().click()
    def get_close_card_section_button(self):
        return self.wait.until(EC.presence_of_element_located(self.close_card_section_button))
    def click_close_card_section_button(self):
        self.get_close_card_section_button().click()
    def is_card_added(self):
        return self.wait.until(EC.presence_of_element_located(self.card_image)).is_displayed()

# 5. Escribir un mensaje para el controlador:
    def get_message_for_driver_field(self):
        return self.wait.until(EC.presence_of_element_located(self.message_for_driver_field))
    def set_message_for_driver_field(self, message_for_driver):
        self.get_message_for_driver_field().send_keys(message_for_driver)
    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

# 6. Pedir una manta y pañuelos:
    def get_blanket_tissues_slider(self):
        return self.wait.until(EC.presence_of_element_located(self.blanket_tissues_slider))
    def click_blanket_tissues_slider(self):
        self.get_blanket_tissues_slider().click()
    def is_blanket_tissues_selected(self):
        checkbox = self.wait.until(EC.presence_of_element_located(self.blanket_tissues_checkbox))
        return checkbox.is_selected()

# 7. Pedir 2 helados:
    def get_ice_cream_counter_plus(self):
        return self.wait.until(EC.presence_of_element_located(self.ice_cream_counter_plus))
    def click_ice_cream_counter_plus(self):
        self.get_ice_cream_counter_plus().click()
    def get_ice_cream_count(self):
        ice_cream_number = self.wait.until(EC.presence_of_element_located(self.ice_cream_counter))
        return int(ice_cream_number.text)

# 8. Aparece el modal para buscar un taxi:
    def get_request_taxi_now_button(self):
        return self.wait.until(EC.presence_of_element_located(self.request_taxi_now_button))
    def click_request_taxi_now_button(self):
        self.get_request_taxi_now_button().click()
    def get_order_progress_details(self):
        return self.wait.until(EC.presence_of_element_located(self.order_progress_details))
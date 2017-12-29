from time import sleep

from pages.base.base_page import BasePage


class FormPage(BasePage):
    def click_display_line_button_sport_overview(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/button')
        sleep(2)

    def get_display_line_number_sport_overview(self):
        return len(list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li')))

    def get_per_display_style_sport_overview(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def click_per_display_input_button(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(2)

    def get_per_display_name_sport_overview(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label' % str(n + 1)).get_attribute(
            'title')

    def get_display_line_name_number_sport_overview(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_sport_overview(self, m):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1)).text

    def click_display_line_button_mileage(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/button')
        sleep(2)

    def get_display_line_number_mileage(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li')))

    def get_per_display_style_mileage(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_mileage(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label' % str(
                n + 1)).get_attribute('title')

    def click_per_display_input_button_mileage(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label' % str(n + 1))
        sleep(2)

    def get_display_line_name_number_mileage(self):
        return len(list(self.driver.get_elements('x,//*[@id="mileageTableHeader"]/thead/tr/th')))

    def get_per_display_name_on_line_mileage(self, m):
        return self.driver.get_element('x,//*[@id="mileageTableHeader"]/thead/tr/th[%s]/div[1]' % str(m + 1)).text

    def click_display_line_button_travel(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/button')
        sleep(2)

    def get_display_line_number_travel(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li')))

    def get_per_display_style_travel(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_travel(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label' % str(
                n + 1)).get_attribute('title')

    def click_display_line_button_overspeed(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/button')
        sleep(2)

    def get_display_line_number_overspeed(self):
        return len(list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li')))

    def get_per_display_style_overspeed(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_overspeed(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label' % str(n + 1)).get_attribute(
            'title')

    def click_per_display_input_button_overspeed(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(n + 1))

    def get_display_line_name_number_overspeed(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_overspeed(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1))

    def click_display_line_button_stay(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/button')
        sleep(2)

    def get_display_line_number_stay(self):
        return len(list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li')))

    def get_per_display_style_stay(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_stay(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label' % str(n + 1)).get_attribute(
            'title')

    def click_per_display_input_button_stay(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1))
        sleep(1)

    def get_display_line_name_number_stay(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_stay(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1))

    def click_display_line_button_stay_not_shutdown(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/button')
        sleep(2)

    def get_display_line_number_stay_not_shutdown(self):
        return len(list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li')))

    def get_per_display_style_stay_not_shutdowm(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_stay_not_shutdown(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label' % str(n + 1)).get_attribute(
            'title')

    def click_per_display_input_button_stay_not_shutdown(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(1)

    def get_display_line_name_number_stay_not_shutdown(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_stay_not_shutdown(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1))

    def click_display_line_button_acc(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/button')
        sleep(2)

    def get_display_line_number_acc(self):
        return len(list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li')))

    def get_per_display_style_acc(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_acc(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label' % str(n + 1)).get_attribute(
            'title')

    def click_per_display_input_button_acc(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1))
        sleep(1)

    def get_display_line_name_number_acc(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_acc(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1))

    def get_display_line_name_number_travel(self):
        return len(list(self.driver.get_elements('x,//*[@id="mileageTableHeader"]/thead/tr/th')))

    def click_display_line_button_status(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/button')
        sleep(2)

    def get_display_line_number_status(self):
        return len(list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li')))

    def get_per_display_style_status(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(n + 1)).is_selected()

    def get_per_display_name_status(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[%s]/label' % str(n + 1)).get_attribute(
            'title')

    def click_per_display_input_button_status(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(1)

    def get_display_line_name_number_status(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_status(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1))

    def click_display_line_button_electric(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/button')
        sleep(2)

    def get_display_line_number_electric(self):
        return len(list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li')))

    def get_per_display_style_electric(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(n + 1)).is_selected()

    def get_per_display_name_electric(self, n):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[%s]/label' % str(n + 1))

    def click_per_display_input_button_electric(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(1)

    def get_display_line_name_number_electric(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_electric(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1))

    def click_display_line_button_oil(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/button')
        sleep(2)

    def get_display_line_number_oil(self):
        return len(list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li')))

    def get_per_display_style_oil(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(n + 1)).is_selected()

    def get_per_display_name_oil(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[%s]/label' % str(n + 1)).get_attribute(
            'title')

    def click_per_display_input_button_oil(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(2)

    def get_display_line_name_number_oil(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_oil(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1))

    def click_display_line_button_alarm_overview(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/button')
        sleep(2)

    def get_display_line_number_alarm_overview(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/ul/li')))

    def get_per_display_style_alarm_overview(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_alarm_overview(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/ul/li[%s]/label' % str(
                n + 1)).get_attribute('title')

    def click_per_display_input_button_alarm_overview(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(2)

    def get_display_line_name_number_alarm_overview(self):
        return len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_alarm_overview(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1))

    def click_display_line_button_alarm_detail(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div/button')
        sleep(2)

    def get_display_line_number_alarm_detail(self):
        return len(list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div/ul/li')))

    def get_per_display_style_alarm_detail(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(n + 1)).is_selected()

    def get_per_display_name_alarm_detail(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div/ul/li[%s]/label' % str(n + 1)).get_attribute(
            'title')

    def click_per_display_input_button_alarm_detail(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(2)

    def get_display_line_name_number_alarm_detail(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_alarm_detail(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(m + 1))

    def click_display_line_button_obd_mileage(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/button')
        sleep(2)

    def get_display_line_number_obd_mileage(self):
        return len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li')))

    def get_per_display_style_obd_mileage(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_obd_mileage(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label' % str(
                n + 1)).get_attribute('title')

    def click_per_display_input_button_obd_mileage(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(
                n + 1))
        sleep(2)

    def get_display_line_name_number_obd_mileage(self):
        return len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_obd_mileage(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(
                m + 1))

    def click_display_line_button_obd_travel(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/button')
        sleep(2)

    def get_display_line_number_obd_travel(self):
        return len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li')))

    def get_per_display_style_obd_travel(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_obd_travel(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label' % str(
                n + 1)).get_attribute('title')

    def click_per_display_input_button_obd_travel(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(
                n + 1))
        sleep(2)

    def get_display_line_name_number_obd_travel(self):
        return len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_obd_travel(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(
                m + 1))

    def click_display_line_button_obd_car_condition(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/button')
        sleep(2)

    def get_per_display_style_obd_car_condition(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_obd_car_condition(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label' % str(
                n + 1)).get_attribute('title')

    def click_per_display_input_button_obd_car_condition(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(
                n + 1))
        sleep(1)

    def get_display_line_name_number_obd_car_condition(self):
        return len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li')))

    def get_per_display_name_on_line_obd_car_condition(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(
                m + 1))

    def click_display_line_button_obd_failure(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/button')
        sleep(2)

    def get_display_line_number_obd_failure(self):
        return len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li')))

    def get_per_display_style_obd_failure(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def get_per_display_name_obd_failure(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label' % str(
                n + 1)).get_attribute('title')

    def click_per_display_input_button_obd_failure(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/ul/li[%s]/label/input' % str(
                n + 1))
        sleep(2)

    def get_display_line_name_number_obd_failure(self):
        return len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]/table/thead/tr/th')))

    def get_per_display_name_on_line_obd_failure(self, m):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]/table/thead/tr/th[%s]/div[1]' % str(
                m + 1))

    def click_display_line_button_mileage_with_day(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/button')
        sleep(2)

    def get_display_line_number_mileage_with_day(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li')))

    def get_per_display_style_mileage_with_day(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def click_per_display_input_button_mileage_with_day(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(1)

    def click_per_display_input_button_travel(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(1)

    def click_display_line_button_travel_with_day(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/button')
        sleep(1)

    def get_display_line_number_travel_with_day(self):
        return len(
            list(self.driver.get_elements('x,/html/body/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li')))

    def get_per_display_style_travel_with_day(self, n):
        return self.driver.get_element(
            'x,/html/body/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(
                n + 1)).is_selected()

    def click_per_display_input_button_travel_with_day(self, n):
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[%s]/label/input' % str(n + 1))
        sleep(1)

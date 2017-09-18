from pages.base.base_page_server import BasePageServer


class AccountCenterNaviBarPage2(BasePageServer):
    def switch_to_feedback_frame(self):
        self.driver.switch_to_frame('x,//*[@id="feedbackReportFrame"]')

    def get_total_numbers_feedback(self):
        return len(list(self.driver.get_elements('x,/html/body/div/div[2]/div/ul/li')))

    def click_per_feedback_in_feedback_page(self, n):
        self.driver.click_element('x,/html/body/div/div[2]/div/ul/li[%s]' % str(n + 1))
        return self.driver.get_element('x,/html/body/div/div[2]/div/ul/li[%s]' % str(n + 1)).get_attribute('class')

    def click_ensuer_button_in_feedback_page(self):
        self.driver.click_element('x,//*[@id="userFeedbackForm"]/div[4]/div/button')

    def get_error_content_in_feedback(self):
        return self.driver.get_text('x,//*[@id="userFeedbackForm"]/div[1]/div/label')

    def get_error_contact_in_feedback(self):
        return self.driver.get_text('x,//*[@id="userFeedbackForm"]/div[2]/div/label')

    def get_error_phone_in_feedback(self):
        return self.driver.get_text('x,//*[@id="userFeedbackForm"]/div[3]/div/label')

    def input_content_after_ensuer_in_feedback_page(self, param):
        self.driver.operate_input_element('x,//*[@id="content"]', param)
        self.driver.click_element('x,//*[@id="userFeedbackForm"]/div[4]/div/button')

    def input_contact_after_ensuer_in_feedback_page(self, param):
        self.driver.operate_input_element('x,//*[@id="linkman"]', param)
        self.driver.click_element('x,//*[@id="userFeedbackForm"]/div[4]/div/button')

    def input_phone_after_ensuer_in_feedback_page(self, param):
        self.driver.operate_input_element('x,//*[@id="phone"]', param)
        self.driver.click_element('x,//*[@id="userFeedbackForm"]/div[4]/div/button')

    def get_feedback_text_after_click_ensuer(self):
        return self.driver.get_text('c,layui-layer-content')

from test_funcs import CamundaTest
import config as cfg

test = CamundaTest()
test.go_to_page(cfg.site)
test.login_camunda(cfg.login, cfg.password)
process_data_list = test.get_dict_from_xls(cfg.data_file)
for process_data in process_data_list:
    test.go_into_process('Открытие счета')
    test.fill_process_form(process_data)
test.finish_test()
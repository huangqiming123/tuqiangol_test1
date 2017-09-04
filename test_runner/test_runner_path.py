class TestRunnerPath(object):
    def test_cases_path(self, name):
        path = 'E:\\git\\tuqiangol_test\\testcases\\%s' % name
        return path

    def test_report_path(self, name):
        # path = '\\\\172.16.0.101\\share\\automate_report\\tuqiangol_test\\%s' % name
        path = 'E:\\git\\tuqiangol_test\\reports\\%s' % name
        return path

def duanyan(httpcodee,success,code,message,respons,self):
    self.assertEqual(httpcodee, respons.status_code)
    self.assertEqual(success, respons.json().get("success"))
    self.assertEqual(code, respons.json().get("code"))
    self.assertIn(message, respons.json().get("message"))
"""
Holds various HTML contract templates.
"""

import os
import cla

class ContractTemplate(object):
    def __init__(self, document_type='Individual', major_version=1, minor_version=0, body=None):
        self.document_type = document_type
        self.major_version = major_version
        self.minor_version = minor_version
        self.body = body

    def get_html_contract(self, legal_entity_name, preamble):
        html = self.body
        if html is not None:
            html = html.replace('{{document_type}}', self.document_type)
            html = html.replace('{{major_version}}', str(self.major_version))
            html = html.replace('{{minor_version}}', str(self.minor_version))
            html = html.replace('{{legal_entity_name}}', legal_entity_name)
            html = html.replace('{{preamble}}', preamble)
        return html

    def get_tabs(self):
        return []

class TestTemplate(ContractTemplate):
    def __init__(self, document_type='Individual', major_version=1, minor_version=0, body=None):
        super().__init__(document_type, major_version, minor_version, body)
        if self.body is None:
            self.body = """
<html>
    <body>
        <h3 class="legal-entity-name" style="text-align: center">
            {{legal_entity_name}}<br />
            {{document_type}} Contributor License Agreement ("Agreement") v{{major_version}}.{{minor_version}}
        </h3>
        <div class="preamble">
            {{preamble}}
        </div>
        <p>If you have not already done so, please complete and sign, then scan and email a pdf file of this Agreement to cla@cncf.io.<br />If necessary, send an original signed Agreement to The Linux Foundation: 1 Letterman Drive, Building D, Suite D4700, San Francisco CA 94129, U.S.A.<br />Please read this document carefully before signing and keep a copy for your records.
        </p>
        <p>You accept and agree to the following terms and conditions for Your present and future Contributions submitted to the Foundation. In return, the Foundation shall not use Your Contributions in a way that is contrary to the public benefit or inconsistent with its nonprofit status and bylaws in effect at the time of the Contribution. Except for the license granted herein to the Foundation and recipients of software distributed by the Foundation, You reserve all right, title, and interest in and to Your Contributions
        </p>
    </body>
</html>"""

class CNCFTemplate(ContractTemplate):
    def __init__(self, document_type='Individual', major_version=1, minor_version=0):
        super().__init__(document_type, major_version, minor_version)
        cwd = os.path.dirname(os.path.realpath(__file__))
        fname = '%s/cncf-%s-cla.html' %(cwd, document_type.lower())
        self.body = open(fname).read()

    def get_tabs(self):
        if self.document_type == 'Individual':
            return [
                {'type': 'text_unlocked',
                 'id': 'full_name',
                 'name': 'Full Name',
                 'position_x': 105,
                 'position_y': 302,
                 'width': 360,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'public_name',
                 'name': 'Public Name',
                 'position_x': 120,
                 'position_y': 330,
                 'width': 345,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'mailing_address_1',
                 'name': 'Mailing Address1',
                 'position_x': 140,
                 'position_y': 358,
                 'width': 325,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'mailing_address_2',
                 'name': 'Mailing Address2',
                 'position_x': 55,
                 'position_y': 386,
                 'width': 420,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'country',
                 'name': 'Country',
                 'position_x': 100,
                 'position_y': 414,
                 'width': 370,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'telephone',
                 'name': 'Telephone',
                 'position_x': 115,
                 'position_y': 442,
                 'width': 350,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'email',
                 'name': 'Email',
                 'position_x': 90,
                 'position_y': 470,
                 'width': 380,
                 'height': 20,
                 'page': 1},
                {'type': 'sign',
                 'id': 'sign',
                 'name': 'Please Sign',
                 'position_x': 180,
                 'position_y': 140,
                 'width': 0,
                 'height': 0,
                 'page': 3},
                {'type': 'date',
                 'id': 'date',
                 'name': 'Date',
                 'position_x': 350,
                 'position_y': 182,
                 'width': 0,
                 'height': 0,
                 'page': 3}
            ]
        else:
            return [
                {'type': 'text',
                 'id': 'corporation_name',
                 'name': 'Corporation Name',
                 'position_x': 148,
                 'position_y': 359,
                 'width': 355,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'corporation_address1',
                 'name': 'Corporation Address',
                 'position_x': 158,
                 'position_y': 387,
                 'width': 340,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'corporation_address2',
                 'name': 'Corporation Address',
                 'position_x': 70,
                 'position_y': 415,
                 'width': 445,
                 'height': 20,
                 'page': 1},
                {'type': 'text_optional',
                 'id': 'corporation_address3',
                 'name': 'Corporation Address',
                 'position_x': 70,
                 'position_y': 443,
                 'width': 445,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'point_of_contact',
                 'name': 'Point of Contact',
                 'position_x': 140,
                 'position_y': 471,
                 'width': 355,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'email',
                 'name': 'Email',
                 'position_x': 98,
                 'position_y': 499,
                 'width': 420,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'telephone',
                 'name': 'Telephone',
                 'position_x': 110,
                 'position_y': 527,
                 'width': 405,
                 'height': 20,
                 'page': 1},
                {'type': 'sign',
                 'id': 'sign',
                 'name': 'Please Sign',
                 'position_x': 180,
                 'position_y': 169,
                 'width': 0,
                 'height': 0,
                 'page': 3},
                {'type': 'date',
                 'id': 'date',
                 'name': 'Date',
                 'position_x': 350,
                 'position_y': 212,
                 'width': 0,
                 'height': 0,
                 'page': 3},
                {'type': 'text_unlocked',
                 'id': 'title',
                 'name': 'Title',
                 'position_x': 85,
                 'position_y': 237,
                 'width': 430,
                 'height': 20,
                 'page': 3},
                {'type': 'text',
                 'id': 'corporation',
                 'name': 'Corporation',
                 'position_x': 120,
                 'position_y': 264,
                 'width': 385,
                 'height': 20,
                 'page': 3},
                 {'type': 'text',
                 'id': 'scheduleA',
                 'name': 'Schedule A',
                 'position_x': 54,
                 'position_y': 147,
                 'width': 550,
                 'height': 600,
                 'page': 4},
                {'type': 'text_optional',
                 'id': 'scheduleB',
                 'name': 'Schedule B',
                 'position_x': 54,
                 'position_y': 147,
                 'width': 550,
                 'height': 600,
                 'page': 5}
            ]

class OpenBMCTemplate(ContractTemplate):
    def __init__(self, document_type='Individual', major_version=1, minor_version=0):
        super().__init__(document_type, major_version, minor_version)
        cwd = os.path.dirname(os.path.realpath(__file__))
        fname = '%s/openbmc-%s-cla.html' %(cwd, document_type.lower())
        self.body = open(fname).read()

    def get_tabs(self):
        if self.document_type == 'Individual':
            return [
                {'type': 'text_unlocked',
                 'id': 'full_name',
                 'name': 'Full Name',
                 'position_x': 105,
                 'position_y': 298,
                 'width': 360,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'public_name',
                 'name': 'Public Name',
                 'position_x': 120,
                 'position_y': 326,
                 'width': 345,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'mailing_address_1',
                 'name': 'Mailing Address1',
                 'position_x': 140,
                 'position_y': 354,
                 'width': 325,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'mailing_address_2',
                 'name': 'Mailing Address2',
                 'position_x': 55,
                 'position_y': 382,
                 'width': 420,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'country',
                 'name': 'Country',
                 'position_x': 100,
                 'position_y': 410,
                 'width': 370,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'telephone',
                 'name': 'Telephone',
                 'position_x': 115,
                 'position_y': 438,
                 'width': 350,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'email',
                 'name': 'Email',
                 'position_x': 90,
                 'position_y': 465,
                 'width': 380,
                 'height': 20,
                 'page': 1},
                {'type': 'sign',
                 'id': 'sign',
                 'name': 'Please Sign',
                 'position_x': 180,
                 'position_y': 120,
                 'width': 0,
                 'height': 0,
                 'page': 3},
                {'type': 'date',
                 'id': 'date',
                 'name': 'Date',
                 'position_x': 350,
                 'position_y': 162,
                 'width': 0,
                 'height': 0,
                 'page': 3}
            ]
        else:
            return [
                {'type': 'text',
                 'id': 'corporation_name',
                 'name': 'Corporation Name',
                 'position_x': 151,
                 'position_y': 355,
                 'width': 355,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'corporation_address1',
                 'name': 'Corporation Address',
                 'position_x': 161,
                 'position_y': 383,
                 'width': 340,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'corporation_address2',
                 'name': 'Corporation Address',
                 'position_x': 73,
                 'position_y': 411,
                 'width': 445,
                 'height': 20,
                 'page': 1},
                {'type': 'text_optional',
                 'id': 'corporation_address3',
                 'name': 'Corporation Address',
                 'position_x': 73,
                 'position_y': 439,
                 'width': 445,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'point_of_contact',
                 'name': 'Point of Contact',
                 'position_x': 144,
                 'position_y': 466,
                 'width': 355,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'email',
                 'name': 'Email',
                 'position_x': 101,
                 'position_y': 494,
                 'width': 420,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'telephone',
                 'name': 'Telephone',
                 'position_x': 113,
                 'position_y': 522,
                 'width': 405,
                 'height': 20,
                 'page': 1},
                {'type': 'sign',
                 'id': 'sign',
                 'name': 'Please Sign',
                 'position_x': 180,
                 'position_y': 153,
                 'width': 0,
                 'height': 0,
                 'page': 3},
                {'type': 'date',
                 'id': 'date',
                 'name': 'Date',
                 'position_x': 362,
                 'position_y': 192,
                 'width': 0,
                 'height': 0,
                 'page': 3},
                {'type': 'text_unlocked',
                 'id': 'title',
                 'name': 'Title',
                 'position_x': 89,
                 'position_y': 221,
                 'width': 430,
                 'height': 20,
                 'page': 3},
                {'type': 'text',
                 'id': 'corporation',
                 'name': 'Corporation',
                 'position_x': 126,
                 'position_y': 249,
                 'width': 385,
                 'height': 20,
                 'page': 3},
                {'type': 'text',
                 'id': 'scheduleA',
                 'name': 'Schedule A',
                 'position_x': 54,
                 'position_y': 147,
                 'width': 550,
                 'height': 600,
                 'page': 4},
                {'type': 'text_optional',
                 'id': 'scheduleB',
                 'name': 'Schedule B',
                 'position_x': 54,
                 'position_y': 147,
                 'width': 550,
                 'height': 600,
                 'page': 5}
            ]


class OpenColorIOTemplate(ContractTemplate):
    def __init__(self, document_type='Individual', major_version=1, minor_version=1):
        super().__init__(document_type, major_version, minor_version)
        cwd = os.path.dirname(os.path.realpath(__file__))
        fname = '%s/opencolorio-%s-cla.html' %(cwd, document_type.lower())
        self.body = open(fname).read()

    def get_tabs(self):
        if self.document_type == 'Individual':
            return [
                {'type': 'sign',
                 'id': 'sign',
                 'name': 'Please Sign',
                 'position_x': 180,
                 'position_y': 317,
                 'width': 0,
                 'height': 0,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'name',
                 'name': 'Name',
                 'position_x': 85,
                 'position_y': 382,
                 'width': 300,
                 'height': 20,
                 'page': 1},
                {'type': 'date',
                 'id': 'date',
                 'name': 'Date',
                 'position_x': 157,
                 'position_y': 412,
                 'width': 0,
                 'height': 0,
                 'page': 1}
            ]
        else:
            return [
                {'type': 'text',
                 'id': 'cla_manager_name',
                 'name': 'CLA Manager Name',
                 'position_x': 86,
                 'position_y': 525,
                 'width': 200,
                 'height': 20,
                 'page': 1},
                {'type': 'text',
                 'id': 'cla_manager_email',
                 'name': 'CLA Manager Email',
                 'position_x': 304,
                 'position_y': 525,
                 'width': 200,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'corporation_name',
                 'name': 'Company Name',
                 'position_x': 135,
                 'position_y': 608,
                 'width': 300,
                 'height': 20,
                 'page': 1},
                {'type': 'sign',
                 'id': 'sign',
                 'name': 'Please Sign',
                 'position_x': 180,
                 'position_y': 603,
                 'width': 0,
                 'height': 0,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'name',
                 'name': 'Name',
                 'position_x': 85,
                 'position_y': 665,
                 'width': 300,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'title',
                 'name': 'Title',
                 'position_x': 78,
                 'position_y': 692,
                 'width': 300,
                 'height': 20,
                 'page': 1},
                {'type': 'date',
                 'id': 'date',
                 'name': 'Date',
                 'position_x': 149,
                 'position_y': 720,
                 'width': 0,
                 'height': 0,
                 'page': 1}
            ]

class TungstenFabricTemplate(ContractTemplate):
    def __init__(self, document_type='Individual', major_version=1, minor_version=0):
        super().__init__(document_type, major_version, minor_version)
        cwd = os.path.dirname(os.path.realpath(__file__))
        fname = '%s/tungsten-fabric-%s-cla.html' %(cwd, document_type.lower())
        self.body = open(fname).read()

    def get_tabs(self):
        if self.document_type == 'Individual':
            return [
                {'type': 'text_unlocked',
                 'id': 'full_name',
                 'name': 'Full Name',
                 'position_x': 105,
                 'position_y': 312,
                 'width': 360,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'public_name',
                 'name': 'Public Name',
                 'position_x': 120,
                 'position_y': 340,
                 'width': 345,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'mailing_address_1',
                 'name': 'Mailing Address1',
                 'position_x': 140,
                 'position_y': 368,
                 'width': 325,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'mailing_address_2',
                 'name': 'Mailing Address2',
                 'position_x': 55,
                 'position_y': 396,
                 'width': 420,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'country',
                 'name': 'Country',
                 'position_x': 100,
                 'position_y': 424,
                 'width': 370,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'telephone',
                 'name': 'Telephone',
                 'position_x': 115,
                 'position_y': 452,
                 'width': 350,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'email',
                 'name': 'Email',
                 'position_x': 90,
                 'position_y': 479,
                 'width': 380,
                 'height': 20,
                 'page': 1},
                {'type': 'sign',
                 'id': 'sign',
                 'name': 'Please Sign',
                 'position_x': 180,
                 'position_y': 140,
                 'width': 0,
                 'height': 0,
                 'page': 3},
                {'type': 'date',
                 'id': 'date',
                 'name': 'Date',
                 'position_x': 350,
                 'position_y': 182,
                 'width': 0,
                 'height': 0,
                 'page': 3}
            ]
        else:
            return [
                {'type': 'text',
                 'id': 'corporation_name',
                 'name': 'Corporation Name',
                 'position_x': 151,
                 'position_y': 368,
                 'width': 355,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'corporation_address1',
                 'name': 'Corporation Address',
                 'position_x': 161,
                 'position_y': 396,
                 'width': 340,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'corporation_address2',
                 'name': 'Corporation Address',
                 'position_x': 73,
                 'position_y': 424,
                 'width': 445,
                 'height': 20,
                 'page': 1},
                {'type': 'text_optional',
                 'id': 'corporation_address3',
                 'name': 'Corporation Address',
                 'position_x': 73,
                 'position_y': 452,
                 'width': 445,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'point_of_contact',
                 'name': 'Point of Contact',
                 'position_x': 144,
                 'position_y': 479,
                 'width': 355,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'email',
                 'name': 'Email',
                 'position_x': 101,
                 'position_y': 507,
                 'width': 420,
                 'height': 20,
                 'page': 1},
                {'type': 'text_unlocked',
                 'id': 'telephone',
                 'name': 'Telephone',
                 'position_x': 113,
                 'position_y': 535,
                 'width': 405,
                 'height': 20,
                 'page': 1},
                {'type': 'sign',
                 'id': 'sign',
                 'name': 'Please Sign',
                 'position_x': 180,
                 'position_y': 167,
                 'width': 0,
                 'height': 0,
                 'page': 3},
                {'type': 'date',
                 'id': 'date',
                 'name': 'Date',
                 'position_x': 364,
                 'position_y': 207,
                 'width': 0,
                 'height': 0,
                 'page': 3},
                {'type': 'text_unlocked',
                 'id': 'title',
                 'name': 'Title',
                 'position_x': 89,
                 'position_y': 234,
                 'width': 430,
                 'height': 20,
                 'page': 3},
                {'type': 'text',
                 'id': 'corporation',
                 'name': 'Corporation',
                 'position_x': 126,
                 'position_y': 262,
                 'width': 385,
                 'height': 20,
                 'page': 3},
                {'type': 'text',
                 'id': 'scheduleA',
                 'name': 'Schedule A',
                 'position_x': 54,
                 'position_y': 147,
                 'width': 550,
                 'height': 600,
                 'page': 4},
                {'type': 'text_optional',
                 'id': 'scheduleB',
                 'name': 'Schedule B',
                 'position_x': 54,
                 'position_y': 147,
                 'width': 550,
                 'height': 600,
                 'page': 5}
            ]

from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc
from constants.styles import TABLE_STYLE, TABLE_CELL_STYLE, TABLE_HEADER_STYLE


# Define Table
# Define Table
table_data = [
    {'ID': '1', 'Company Name': '5 Seconds Advertising', 'Contact Person': 'Bocs Lina', 'Contact No.': '0917-849-0782', 'Email Address': 'N/A', },
    {'ID': '2', 'Company Name': 'Asia (Tianjin) Steel Co., Ltd', 'Contact Person': 'Juju', 'Contact No.': '', 'Email Address': '', },
    {'ID': '3', 'Company Name': 'Ateneo De Manila University', 'Contact Person': 'Johanna M. Santos', 'Contact No.': '', 'Email Address': '', },
    {'ID': '4', 'Company Name': 'Beaucon', 'Contact Person': 'Liz Tan', 'Contact No.': '', 'Email Address': '', },
    {'ID': '5', 'Company Name': 'Bluefish Asia Events & Media', 'Contact Person': 'Kathleen Cervantes', 'Contact No.': '0917-521-3899', 'Email Address': 'katcervantes@bluefish-asia.com', },
    {'ID': '6', 'Company Name': 'Century Exhibition Group (VN) Ltd', 'Contact Person': 'Helen Hu', 'Contact No.': '', 'Email Address': '', },
    {'ID': '7', 'Company Name': 'Chuangji Exhibition', 'Contact Person': 'Leo Wang', 'Contact No.': '', 'Email Address': '', },
    {'ID': '8', 'Company Name': 'City Trade And Industry Dept. Calapan', 'Contact Person': 'Joanne Leynes', 'Contact No.': '0943-329-8896', 'Email Address': 'joanne.leynes@yahoo.com', },
    {'ID': '9', 'Company Name': 'Cityneon Philippines Inc', 'Contact Person': 'Patrick Tirado', 'Contact No.': '0920-986-0408', 'Email Address': 'N/A', },
    {'ID': '10', 'Company Name': 'Colorsteel', 'Contact Person': 'Jaco', 'Contact No.': '', 'Email Address': '', },
    {'ID': '11', 'Company Name': 'Department Of Migrant Workers', 'Contact Person': 'Neil Burdeos', 'Contact No.': '0917-806-3288', 'Email Address': 'N/A', },
    {'ID': '12', 'Company Name': 'DOST', 'Contact Person': 'Angelito T. Uldo', 'Contact No.': '0916-264-8314', 'Email Address': 'N/A', },
    {'ID': '13', 'Company Name': 'Dusit Hotels & Resort In Davao', 'Contact Person': 'Jennifer Tuballes', 'Contact No.': '0995-177-6068', 'Email Address': 'N/A', },
    {'ID': '14', 'Company Name': 'Easy Brand', 'Contact Person': 'Andrea Galope', 'Contact No.': '', 'Email Address': '', },
    {'ID': '15', 'Company Name': 'Edwin D. Uy Architecture Interior & Design Office', 'Contact Person': 'Michael John A. Laviste', 'Contact No.': '0917-596-0280', 'Email Address': 'mj.laviste@edwinuy.ph', },
    {'ID': '16', 'Company Name': 'Engagement By Elle Inc.', 'Contact Person': 'Larizze Bonifacio', 'Contact No.': '0966-210-0620', 'Email Address': 'N/A', },
    {'ID': '17', 'Company Name': 'Eventscape Manila', 'Contact Person': 'Charles Quiazon', 'Contact No.': '0905-462-5124', 'Email Address': 'N/A', },
    {'ID': '18', 'Company Name': 'FBC Tycoon', 'Contact Person': 'Florentino Calzado', 'Contact No.': '0919-002-5687', 'Email Address': 'N/A', },
    {'ID': '19', 'Company Name': 'FEU Manila', 'Contact Person': 'Kathleen Lazaro', 'Contact No.': '', 'Email Address': '', },
    {'ID': '20', 'Company Name': 'FRLD, Inc.', 'Contact Person': 'Sally Mecija', 'Contact No.': '', 'Email Address': '', },
    {'ID': '21', 'Company Name': 'Grace Exposition International Services', 'Contact Person': 'Grace Aguilar', 'Contact No.': '', 'Email Address': '', },
    {'ID': '22', 'Company Name': 'Grand Philippines', 'Contact Person': 'Jeffrey Tan', 'Contact No.': '0933-247-6955', 'Email Address': 'grandphilippines@gmail.com', },
    {'ID': '23', 'Company Name': 'Guang Jia Hua Aluminum Co., Ltd', 'Contact Person': 'Juju', 'Contact No.': '', 'Email Address': '', },
    {'ID': '24', 'Company Name': 'Gulf Oil Philippines', 'Contact Person': 'Sheila Anne B. Padon', 'Contact No.': '0995-091-0449', 'Email Address': 'N/A', },
    {'ID': '25', 'Company Name': 'Haohan International Exhibition Co., Ltd.', 'Contact Person': 'Elsa Feng', 'Contact No.': '', 'Email Address': '', },
    {'ID': '26', 'Company Name': 'Hue Hotels And Resorts ( Luana Lifestyle And Leisure Hotel Inc)', 'Contact Person': 'Ara Sucaldito', 'Contact No.': '0966-192-9209', 'Email Address': 'asucaldito@thehuehotel.com', },
    {'ID': '27', 'Company Name': 'I Am World Corporation', 'Contact Person': 'Edwin Cano', 'Contact No.': 'N/A', 'Email Address': 'N/A', },
    {'ID': '28', 'Company Name': 'Inside Racing', 'Contact Person': 'Jennifer Morente', 'Contact No.': '', 'Email Address': '', },
    {'ID': '29', 'Company Name': 'Lighthouse Events', 'Contact Person': 'Zaldariaga', 'Contact No.': 'N/A', 'Email Address': 'N/A', },
    {'ID': '30', 'Company Name': 'LX Development Group Ltd.', 'Contact Person': 'Jason Chong', 'Contact No.': '', 'Email Address': '', },
    {'ID': '31', 'Company Name': 'Makeitive', 'Contact Person': 'Arnold Cabales', 'Contact No.': '0998-990-0069', 'Email Address': 'N/A', },
    {'ID': '32', 'Company Name': 'Mediacom Solutions Inc', 'Contact Person': 'Margo Quadra', 'Contact No.': '', 'Email Address': '', },
    {'ID': '33', 'Company Name': 'NAITAS', 'Contact Person': 'Macky B. Soriano', 'Contact No.': '0917-558-1942', 'Email Address': 'mackybsoriano@gmail.com', },
    {'ID': '34', 'Company Name': 'NBDB', 'Contact Person': 'NBDB', 'Contact No.': '', 'Email Address': '', },
    {'ID': '35', 'Company Name': 'PFA', 'Contact Person': 'Christopher Lim', 'Contact No.': '', 'Email Address': '', },
    {'ID': '36', 'Company Name': 'Philippine Coal Plant Group Inc.', 'Contact Person': 'Raquel', 'Contact No.': '', 'Email Address': '', },
    {'ID': '37', 'Company Name': 'Philippine Coffee Guild', 'Contact Person': 'Philippine Coffee Guild', 'Contact No.': '', 'Email Address': '', },
    {'ID': '38', 'Company Name': 'Philippine Textile Research Institute', 'Contact Person': 'Angelito T. Uldo', 'Contact No.': '0916-264-8314', 'Email Address': 'N/A', },
    {'ID': '39', 'Company Name': 'PIDSIP', 'Contact Person': 'Mary Manese', 'Contact No.': '0915-087-9966', 'Email Address': 'N/A', },
    {'ID': '40', 'Company Name': 'Prima Enterprise', 'Contact Person': 'Benjamin Gokingyok', 'Contact No.': '0962-217-8864', 'Email Address': 'c.elon@primal.com.ph, mktg-1@prima.com.ph', },
    {'ID': '41', 'Company Name': 'Primal Eneterprises Corp.', 'Contact Person': 'Katerina', 'Contact No.': '0962-217-8864', 'Email Address': 'c.elon@primal.com.ph, mktg-1@primal.com.ph', },
    {'ID': '42', 'Company Name': 'Profilm- Top Innovations Inc', 'Contact Person': 'Fhoebie De Vera', 'Contact No.': '0917-658-0952', 'Email Address': 'N/A', },
    {'ID': '43', 'Company Name': 'Propak Philippines', 'Contact Person': 'Ooi Xiao Hui', 'Contact No.': '0916-335-1598', 'Email Address': 'xiaohui@es-corp.co', },
    {'ID': '44', 'Company Name': 'PSME Foundation', 'Contact Person': 'Shiela Irlandez', 'Contact No.': '0917-550-0002', 'Email Address': 'N/A', },
    {'ID': '45', 'Company Name': 'Quiplist Events Production, Inc.', 'Contact Person': 'Kate Gatchalian', 'Contact No.': '0965-877-1856', 'Email Address': 'prod.quiplist@gmail.com', },
    {'ID': '46', 'Company Name': 'Rage - Top Innovations Inc.', 'Contact Person': 'Fhoebie De Vera', 'Contact No.': '0917-658-0952', 'Email Address': 'N/A', },
    {'ID': '47', 'Company Name': 'RGM Events Management', 'Contact Person': 'Michelle Hilaga', 'Contact No.': '0908-817-9872', 'Email Address': 'N/A', },
    {'ID': '48', 'Company Name': 'Semiconductor And Electronics Industries In The Philippines Foundation', 'Contact Person': 'Cristjan Dave Bael', 'Contact No.': '', 'Email Address': '', },
    {'ID': '49', 'Company Name': 'Sofitel Harbor Sector Meeting', 'Contact Person': 'Sherrald Osarman', 'Contact No.': '0945-829-0188', 'Email Address': 'N/A', },
    {'ID': '50', 'Company Name': 'Summit Media', 'Contact Person': 'Aileen Camansag', 'Contact No.': '0966-204-6024', 'Email Address': 'aileen.camansag@summitmedia.com.ph', },
    {'ID': '51', 'Company Name': 'Tenbuild Trading Corp', 'Contact Person': 'Joyce Lim', 'Contact No.': '', 'Email Address': '', },
    {'ID': '52', 'Company Name': 'The Wedding Library', 'Contact Person': 'Winnie Natividad', 'Contact No.': 'N/A', 'Email Address': 'N/A', },
    {'ID': '53', 'Company Name': 'TME', 'Contact Person': 'Monica Anne Dela Cruz', 'Contact No.': '', 'Email Address': '', },
    {'ID': '54', 'Company Name': 'Top Joy', 'Contact Person': 'Juju', 'Contact No.': '', 'Email Address': '', },
    {'ID': '55', 'Company Name': 'Travel Tour Expo 2024', 'Contact Person': 'Marjorie Gatungay', 'Contact No.': '0917-859-9545', 'Email Address': 'mgatungay@zurihotel@iloilo.com', },
    {'ID': '56', 'Company Name': 'Uniglobal', 'Contact Person': 'Praveen', 'Contact No.': '91 9560037594', 'Email Address': 'N/A', },
    {'ID': '57', 'Company Name': 'Unioil Petroluem Philippines, Inc', 'Contact Person': 'Edel Myrrh Faith Cipriani', 'Contact No.': '0995-091-0449', 'Email Address': 'N/A', },
    {'ID': '58', 'Company Name': 'United Architects Of The Philippines', 'Contact Person': 'Evelyn Franco', 'Contact No.': '(8)888-9266', 'Email Address': 'N/A', },
    {'ID': '59', 'Company Name': 'University Of Asia And The Pacific', 'Contact Person': 'Ayza Figaro', 'Contact No.': '', 'Email Address': '', },
    {'ID': '60', 'Company Name': 'University Of The Philippines, Office Of International Linkage, Diliman', 'Contact Person': 'Ariane Francisco', 'Contact No.': '0967-698-0208', 'Email Address': 'apfrancisco4@up.edu.ph', },
    {'ID': '61', 'Company Name': 'Visulaunch', 'Contact Person': 'Sarah Jane Chua', 'Contact No.': '', 'Email Address': '', },
    {'ID': '62', 'Company Name': 'Wedding And Beyond', 'Contact Person': 'Tet Chua', 'Contact No.': 'N/A', 'Email Address': 'N/A', },
    {'ID': '63', 'Company Name': 'Weida', 'Contact Person': 'Sky', 'Contact No.': '', 'Email Address': '', },
    {'ID': '64', 'Company Name': 'Westlines Design Technologies Corp.', 'Contact Person': 'Ben Mangiliman', 'Contact No.': '0917-813-3740', 'Email Address': 'arjcr@westlines.design', },
    {'ID': '65', 'Company Name': 'White North Edutech Inc', 'Contact Person': 'Daine Ruth Morales', 'Contact No.': '0915-997-1929', 'Email Address': 'info@canadaeducationfair.ca', },
    {'ID': '66', 'Company Name': 'WMOC Events Mgmt Services', 'Contact Person': 'Lot Ann', 'Contact No.': '', 'Email Address': '', },
    {'ID': '67', 'Company Name': 'WSI', 'Contact Person': 'Jill Ang', 'Contact No.': 'N/A', 'Email Address': 'jill.worldbex@gmail.com', },
    {'ID': '68', 'Company Name': 'Xms Marketing Services', 'Contact Person': 'Pam Valmonte', 'Contact No.': '', 'Email Address': '', },
    {'ID': '69', 'Company Name': 'Zivent-Top Innovations Inc', 'Contact Person': 'Fhoebie De Vera', 'Contact No.': '0917-658-0952', 'Email Address': 'N/A', },
    {'ID': '70', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '71', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '72', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '73', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '74', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '75', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '76', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '77', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '78', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '79', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', },
    {'ID': '80', 'Company Name': '', 'Contact Person': '', 'Contact No.': '', 'Email Address': '', }
] 

table_columns = [
    {'name': 'ID', 'id' : 'ID'},
    {'name': 'Company Name', 'id' : 'Company Name'},
    {'name': 'Contact Person', 'id' : 'Contact Person'},
    {'name': 'Contact No.', 'id' : 'Contact No.'},
    {'name': 'Email Address', 'id' : 'Email Address'},
    
]


def render() -> dbc.Col:
    return dbc.Col([
    dbc.Row([
        dbc.Col(html.H3("Client List:", style={'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), width=2, className="d-flex align-items-center"),
    ]),

    dbc.Row([
        dbc.Col(dash_table.DataTable(
            id='client-table',
            columns=table_columns,
            data=table_data,
            editable=False,
            page_size=10,
            style_table=TABLE_STYLE,
            style_cell=TABLE_CELL_STYLE,
            style_header=TABLE_HEADER_STYLE,
        ), width=12),
    ]),
    
], width=10, style={'margin-top': '20px', 'height': '100%', 'width': '100%'})
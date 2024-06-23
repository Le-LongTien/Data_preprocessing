import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv('diem_thi_thpt_2022.csv')

# Lọc dữ liệu với sbd từ 50 đến 54
#lọc 50->54 từ khắp cả nước
loc_data = data[data['sbd'].between(50000000, 54999999)]
#lọc 5 tỉnh
loc_tinh1 = loc_data[loc_data['sbd'].between(50000000, 50999999)]
loc_tinh2 = loc_data[loc_data['sbd'].between(51000000, 51999999)]
loc_tinh3 = loc_data[loc_data['sbd'].between(52000000, 52999999)]
loc_tinh4 = loc_data[loc_data['sbd'].between(53000000, 53999999)]
loc_tinh5 = loc_data[loc_data['sbd'].between(54000000, 54999999)]

# Xóa các học sinh có dữ liệu tất cả các môn học là NaN(không thi môn nào)
#tạo danh sách
list_of_subject = ['toan','vat_li','hoa_hoc','ngu_van','ngoai_ngu','sinh_hoc','lich_su','dia_li','gdcd']
loc_data.dropna(subset=list_of_subject, how='all', inplace=True)

#chuyển các môn thi sinh không thi có điểm NaN thành -1
data_new = loc_data.fillna(-1)
data_tinh1 = loc_tinh1.fillna(-1)
data_tinh2 = loc_tinh2.fillna(-1)
data_tinh3 = loc_tinh3.fillna(-1)
data_tinh4 = loc_tinh4.fillna(-1)
data_tinh5 = loc_tinh5.fillna(-1)
loc_data = loc_data[loc_data[list_of_subject] != -1].dropna()

#tổng số học sinh đi thi
Tong = data_new[data_new['sbd']>=0].count()['sbd']
print('Tong so thi sinh: ', Tong)

#tổng số học sinh đi thi thi toán,lý, hóa,.......gdcd của từng tỉnh
tinh1 = data_tinh1[data_tinh1['sbd']>=-1].count()['sbd']
print('Tong so thi sinh di thi cua Tinh 50: ', tinh1)
tinh2 = data_tinh2[data_tinh2['sbd']>=-1].count()['sbd']
print('Tong so thi sinh di thi cua Tinh 51: ', tinh2)
tinh3 = data_tinh3[data_tinh3['sbd']>=-1].count()['sbd']
print('Tong so thi sinh di thi cua Tinh 52: ', tinh3)
tinh4 = data_tinh4[data_tinh4['sbd']>=-1].count()['sbd']
print('Tong so thi sinh di thi cua Tinh 53: ', tinh4)
tinh5 = data_tinh5[data_tinh5['sbd']>=-1].count()['sbd']
print('Tong so thi sinh di thi cua Tinh 54: ', tinh5)

#điểm trung bình từng môn của cả 5 tỉnh
DTB_toan = data_new[data_new['toan'] >= 0]['toan'].mean()
DTB_ly = data_new[data_new['vat_li'] >= 0]['vat_li'].mean()
DTB_van = data_new[data_new['ngu_van'] >= 0]['ngu_van'].mean()
DTB_AV = data_new[data_new['ngoai_ngu'] >= 0]['ngoai_ngu'].mean()
DTB_hoa = data_new[data_new['hoa_hoc'] >= 0]['hoa_hoc'].mean()
DTB_sinh = data_new[data_new['sinh_hoc'] >= 0]['sinh_hoc'].mean()
DTB_su = data_new[data_new['lich_su'] >= 0]['lich_su'].mean()
DTB_dia = data_new[data_new['dia_li'] >= 0]['dia_li'].mean()
DTB_gdcd = data_new[data_new['gdcd'] >= 0]['gdcd'].mean()

#Hiển thị kết quả
print('Điểm trung bình môn Toán (5 tỉnh):', DTB_toan)
print('Điểm trung bình môn Lý (5 tỉnh):', DTB_ly)
print('Điểm trung bình môn Hóa (5 tỉnh):', DTB_hoa)
print('Điểm trung bình môn Văn (5 tỉnh):', DTB_van)
print('Điểm trung bình môn Anh Văn (5 tỉnh):', DTB_AV)
print('Điểm trung bình môn Sinh (5 tỉnh):', DTB_sinh)
print('Điểm trung bình môn Sử (5 tỉnh):', DTB_su)
print('Điểm trung bình môn Địa (5 tỉnh):', DTB_dia)
print('Điểm trung bình môn GDCD (5 tỉnh):', DTB_gdcd)

#điểm trung bình từng môn của mỗi tỉnh
#tinh1
DTB_toan1 = data_tinh1[data_tinh1['toan'] >= 0]['toan'].mean()
DTB_ly1 = data_tinh1[data_tinh1['vat_li'] >= 0]['vat_li'].mean()
DTB_van1 = data_tinh1[data_tinh1['ngu_van'] >= 0]['ngu_van'].mean()
DTB_AV1 = data_tinh1[data_tinh1['ngoai_ngu'] >= 0]['ngoai_ngu'].mean()
DTB_hoa1 = data_tinh1[data_tinh1['hoa_hoc'] >= 0]['hoa_hoc'].mean()
DTB_sinh1 = data_tinh1[data_tinh1['sinh_hoc'] >= 0]['sinh_hoc'].mean()
DTB_su1 = data_tinh1[data_tinh1['lich_su'] >= 0]['lich_su'].mean()
DTB_dia1 = data_tinh1[data_tinh1['dia_li'] >= 0]['dia_li'].mean()
DTB_gdcd1 = data_tinh1[data_tinh1['gdcd'] >= 0]['gdcd'].mean()

#Hiển thị kết quả
print('Điểm trung bình môn Toán (tỉnh 50):', DTB_toan1)
print('Điểm trung bình môn Lý (tỉnh 50):', DTB_ly1)
print('Điểm trung bình môn Hóa (tỉnh 50):', DTB_hoa1)
print('Điểm trung bình môn Văn (tỉnh 50):', DTB_van1)
print('Điểm trung bình môn Anh Văn (tỉnh 50):', DTB_AV1)
print('Điểm trung bình môn Sinh (tỉnh 50):', DTB_sinh1)
print('Điểm trung bình môn Sử (tỉnh 50):', DTB_su1)
print('Điểm trung bình môn Địa (tỉnh 50):', DTB_dia1)
print('Điểm trung bình môn GDCD (tỉnh 50):', DTB_gdcd1)

#tỉnh 2
DTB_toan2 = data_tinh2[data_tinh2['toan'] >= 0]['toan'].mean()
DTB_ly2 = data_tinh2[data_tinh2['vat_li'] >= 0]['vat_li'].mean()
DTB_van2 = data_tinh2[data_tinh2['ngu_van'] >= 0]['ngu_van'].mean()
DTB_AV2 = data_tinh2[data_tinh2['ngoai_ngu'] >= 0]['ngoai_ngu'].mean()
DTB_hoa2 = data_tinh2[data_tinh2['hoa_hoc'] >= 0]['hoa_hoc'].mean()
DTB_sinh2 = data_tinh2[data_tinh2['sinh_hoc'] >= 0]['sinh_hoc'].mean()
DTB_su2 = data_tinh2[data_tinh2['lich_su'] >= 0]['lich_su'].mean()
DTB_dia2 = data_tinh2[data_tinh2['dia_li'] >= 0]['dia_li'].mean()
DTB_gdcd2 = data_tinh2[data_tinh2['gdcd'] >= 0]['gdcd'].mean()

#Hiển thị kết quả
print('Điểm trung bình môn Toán (tỉnh 51):', DTB_toan2)
print('Điểm trung bình môn Lý (tỉnh 51):', DTB_ly2)
print('Điểm trung bình môn Hóa (tỉnh 51):', DTB_hoa2)
print('Điểm trung bình môn Văn (tỉnh 51):', DTB_van2)
print('Điểm trung bình môn Anh Văn (tỉnh 51):', DTB_AV2)
print('Điểm trung bình môn Sinh (tỉnh 51):', DTB_sinh2)
print('Điểm trung bình môn Sử (tỉnh 51):', DTB_su2)
print('Điểm trung bình môn Địa (tỉnh 51):', DTB_dia2)
print('Điểm trung bình môn GDCD (tỉnh 51):', DTB_gdcd2)

#tỉnh 3
DTB_toan3 = data_tinh3[data_tinh3['toan'] >= 0]['toan'].mean()
DTB_ly3 = data_tinh3[data_tinh3['vat_li'] >= 0]['vat_li'].mean()
DTB_van3 = data_tinh3[data_tinh3['ngu_van'] >= 0]['ngu_van'].mean()
DTB_AV3 = data_tinh3[data_tinh3['ngoai_ngu'] >= 0]['ngoai_ngu'].mean()
DTB_hoa3 = data_tinh3[data_tinh3['hoa_hoc'] >= 0]['hoa_hoc'].mean()
DTB_sinh3 = data_tinh3[data_tinh3['sinh_hoc'] >= 0]['sinh_hoc'].mean()
DTB_su3 = data_tinh3[data_tinh3['lich_su'] >= 0]['lich_su'].mean()
DTB_dia3 = data_tinh3[data_tinh3['dia_li'] >= 0]['dia_li'].mean()
DTB_gdcd3 = data_tinh3[data_tinh3['gdcd'] >= 0]['gdcd'].mean()

#Hiển thị kết quả
print('Điểm trung bình môn Toán (tỉnh 52):', DTB_toan3)
print('Điểm trung bình môn Lý (tỉnh 52):', DTB_ly3)
print('Điểm trung bình môn Hóa (tỉnh 52):', DTB_hoa3)
print('Điểm trung bình môn Văn (tỉnh 52):', DTB_van3)
print('Điểm trung bình môn Anh Văn (tỉnh 52):', DTB_AV3)
print('Điểm trung bình môn Sinh (tỉnh 52):', DTB_sinh3)
print('Điểm trung bình môn Sử (tỉnh 52):', DTB_su3)
print('Điểm trung bình môn Địa (tỉnh 52):', DTB_dia3)
print('Điểm trung bình môn GDCD (tỉnh 52):', DTB_gdcd3)

#tỉnh 4
DTB_toan4 = data_tinh4[data_tinh4['toan'] >= 0]['toan'].mean()
DTB_ly4 = data_tinh4[data_tinh4['vat_li'] >= 0]['vat_li'].mean()
DTB_van4 = data_tinh4[data_tinh4['ngu_van'] >= 0]['ngu_van'].mean()
DTB_AV4 = data_tinh4[data_tinh4['ngoai_ngu'] >= 0]['ngoai_ngu'].mean()
DTB_hoa4 = data_tinh4[data_tinh4['hoa_hoc'] >= 0]['hoa_hoc'].mean()
DTB_sinh4 = data_tinh4[data_tinh4['sinh_hoc'] >= 0]['sinh_hoc'].mean()
DTB_su4 = data_tinh4[data_tinh4['lich_su'] >= 0]['lich_su'].mean()
DTB_dia4 = data_tinh4[data_tinh4['dia_li'] >= 0]['dia_li'].mean()
DTB_gdcd4 = data_tinh4[data_tinh4['gdcd'] >= 0]['gdcd'].mean()

#Hiển thị kết quả
print('Điểm trung bình môn Toán (tỉnh 53):', DTB_toan4)
print('Điểm trung bình môn Lý (tỉnh 53):', DTB_ly4)
print('Điểm trung bình môn Hóa (tỉnh 53):', DTB_hoa4)
print('Điểm trung bình môn Văn (tỉnh 53):', DTB_van4)
print('Điểm trung bình môn Anh Văn (tỉnh 53):', DTB_AV4)
print('Điểm trung bình môn Sinh (tỉnh 53):', DTB_sinh4)
print('Điểm trung bình môn Sử (tỉnh 53):', DTB_su4)
print('Điểm trung bình môn Địa (tỉnh 53):', DTB_dia4)
print('Điểm trung bình môn GDCD (tỉnh 53):', DTB_gdcd4)

#tỉnh 5
DTB_toan5 = data_tinh5[data_tinh5['toan'] >= 0]['toan'].mean()
DTB_ly5 = data_tinh5[data_tinh5['vat_li'] >= 0]['vat_li'].mean()
DTB_van5 = data_tinh5[data_tinh5['ngu_van'] >= 0]['ngu_van'].mean()
DTB_AV5 = data_tinh5[data_tinh5['ngoai_ngu'] >= 0]['ngoai_ngu'].mean()
DTB_hoa5 = data_tinh5[data_tinh5['hoa_hoc'] >= 0]['hoa_hoc'].mean()
DTB_sinh5 = data_tinh5[data_tinh5['sinh_hoc'] >= 0]['sinh_hoc'].mean()
DTB_su5 = data_tinh5[data_tinh5['lich_su'] >= 0]['lich_su'].mean()
DTB_dia5 = data_tinh5[data_tinh5['dia_li'] >= 0]['dia_li'].mean()
DTB_gdcd5 = data_tinh5[data_tinh5['gdcd'] >= 0]['gdcd'].mean()

#Hiển thị kết quả
print('Điểm trung bình môn Toán (tỉnh 54):', DTB_toan5)
print('Điểm trung bình môn Lý (tỉnh 54):', DTB_ly5)
print('Điểm trung bình môn Hóa (tỉnh 54):', DTB_hoa5)
print('Điểm trung bình môn Văn (tỉnh 54):', DTB_van5)
print('Điểm trung bình môn Anh Văn (tỉnh 54):', DTB_AV5)
print('Điểm trung bình môn Sinh (tỉnh 54):', DTB_sinh5)
print('Điểm trung bình môn Sử (tỉnh 54):', DTB_su5)
print('Điểm trung bình môn Địa (tỉnh 54):', DTB_dia5)
print('Điểm trung bình môn GDCD (tỉnh 54):', DTB_gdcd5)

labels = ['Toán','Lý','Hóa','Văn','Anh Văn','Sinh','Sử','Địa','GDCD'] #cột
values1 = [DTB_toan1, DTB_ly1, DTB_hoa1, DTB_van1, DTB_AV1, DTB_sinh1, DTB_su1, DTB_dia1, DTB_gdcd1] #giá trị
values2 = [DTB_toan2, DTB_ly2, DTB_hoa2, DTB_van2, DTB_AV2, DTB_sinh2, DTB_su2, DTB_dia2, DTB_gdcd2]
values3 = [DTB_toan3, DTB_ly3, DTB_hoa3, DTB_van3, DTB_AV3, DTB_sinh3, DTB_su3, DTB_dia3, DTB_gdcd3]
values4 = [DTB_toan4, DTB_ly4, DTB_hoa4, DTB_van4, DTB_AV4, DTB_sinh4, DTB_su4, DTB_dia4, DTB_gdcd4]
values5 = [DTB_toan5, DTB_ly5, DTB_hoa5, DTB_van5, DTB_AV5, DTB_sinh5, DTB_su5, DTB_dia5, DTB_gdcd5]

#phân tích điểm từng môn riêng lẻ: vẽ 5 biểu đồ cột phân tích năng suất của từng môn của mỗi tỉnh của học sinh: gồm có 5 tỉnh,12 môn
#tỉnh 50
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'yellow']
plt.bar(labels,values1, color = colors)
plt.title('Điểm trung bình môn tỉnh Đồng Tháp')
plt.xlabel('Môn học')
plt.ylabel('Điểm trung bình')
for index, value in enumerate(values1):
    plt.text((index),(value),f'{value:.1f}')
    # plt.text(index, value, f'{value:.1f}', ha='center', va='bottom')
plt.show()

#tỉnh 51
plt.bar(labels,values2, color = colors)
plt.title('Điểm trung bình môn tỉnh An Giang')
plt.xlabel('Môn học')
plt.ylabel('Điểm trung bình')
for index, value in enumerate(values2):
    plt.text((index),(value),f'{value:.1f}')
plt.show()

#tỉnh 52
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'yellow']
plt.bar(labels,values3, color = colors)
plt.title('Điểm trung bình môn tỉnh Bà Rịa')
plt.xlabel('Môn học')
plt.ylabel('Điểm trung bình')
for index, value in enumerate(values3):
    plt.text((index),(value),f'{value:.1f}')
plt.show()

#tỉnh 53
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'yellow']
plt.bar(labels,values4, color = colors)
plt.title('Điểm trung bình các tỉnh Tiền Giang')
plt.xlabel('Môn học')
plt.ylabel('Điểm trung bình')
for index, value in enumerate(values4):
    plt.text((index),(value),f'{value:.1f}')
plt.show()

#tỉnh 54 
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'yellow']
plt.bar(labels,values5, color = colors)
plt.title('Điểm trung bình các tỉnh Kiên Giang')
plt.xlabel('Môn học')
plt.ylabel('Điểm trung bình')
for index, value in enumerate(values5):
    plt.text((index),(value),f'{value:.1f}')
plt.show()

#vẽ biểu đồ đường giữa so sánh điểm trung bình 12 môn của 5 tỉnh
labels = ['Toán','Lý','Hóa','Văn','Anh Văn','Sinh','Sử','Địa','GDCD'] #cột
values = [DTB_toan, DTB_ly, DTB_hoa, DTB_van, DTB_AV, DTB_sinh, DTB_su, DTB_dia, DTB_gdcd] #giá trị
plt.plot(labels, values, marker='o', color='blue')
plt.title('Biểu đồ điểm trung bình môn của 5 tỉnh')
plt.ylabel('Điểm trung bình')
for index, value in enumerate(values):
    plt.text((index),(value),f'{value:.1f}')
plt.show()

# Vẽ biểu đồ đường điểm trung bình từng môn của mỗi tỉnh
#y/c: vẽ chung năm đường vào một đồ thị
plt.plot(labels, values1, marker='x', color='blue', label = 'ĐỒNG THÁP(50)')
plt.plot(labels, values2, marker='o', color='red', label = 'AN GIANG(51)')
plt.plot(labels, values3, marker='.', color='yellow', label = 'BRVT(52)')
plt.plot(labels, values4, marker='+', color='grey', label = 'TIỀN GIANG(53)')
plt.plot(labels, values5, marker='*', color='green', label = 'KIÊN GIANG(54)')

plt.title('Biểu đồ điểm trung bình từng môn của 5 tỉnh')
plt.ylabel('Điểm trung bình')
plt.legend()  # Hiển thị chú thích về các đường
plt.tight_layout()
plt.show()

#biểu đồ phân tán điểm trung bình từng môn của mỗi tỉnh
labels = ['Toán', 'Lý', 'Hóa', 'Văn', 'Anh Văn', 'Sinh', 'Sử', 'Địa', 'GDCD']  # Tên các môn học
values = [
    [DTB_toan1, DTB_ly1, DTB_hoa1, DTB_van1, DTB_AV1, DTB_sinh1, DTB_su1, DTB_dia1, DTB_gdcd1],  # Điểm trung bình của tỉnh 1
    [DTB_toan2, DTB_ly2, DTB_hoa2, DTB_van2, DTB_AV2, DTB_sinh2, DTB_su2, DTB_dia2, DTB_gdcd2],  # Điểm trung bình của tỉnh 2
    [DTB_toan3, DTB_ly3, DTB_hoa3, DTB_van3, DTB_AV3, DTB_sinh3, DTB_su3, DTB_dia3, DTB_gdcd3],  # Điểm trung bình của tỉnh 3
    [DTB_toan4, DTB_ly4, DTB_hoa4, DTB_van4, DTB_AV4, DTB_sinh4, DTB_su4, DTB_dia4, DTB_gdcd4],  # Điểm trung bình của tỉnh 4
    [DTB_toan5, DTB_ly5, DTB_hoa5, DTB_van5, DTB_AV5, DTB_sinh5, DTB_su5, DTB_dia5, DTB_gdcd5]   # Điểm trung bình của tỉnh 5
]

# Danh sách các marker tương ứng với từng tỉnh
markers = ['o', 's', '^', 'x', 'D']

# Vẽ biểu đồ scatterplot
plt.figure(figsize=(10, 6))
for i in range(len(values)):
    plt.scatter(labels, values[i], label=f'Tỉnh {i+1}', marker=markers[i])

plt.xlabel('Môn học')
plt.ylabel('Điểm trung bình')
plt.title('Điểm trung bình môn của các tỉnh')
plt.legend()
plt.xticks(rotation=45)  # Xoay nhãn trục x để dễ đọc hơn
plt.grid(True)

plt.tight_layout()
plt.show()

#biểu đồ tròn: phần trăm thí sinh theo khối tự nhiên và xã hội của 5 tỉnh
#lọc những thí sinh tham gia của từng môn tổ hợp
loc_TN = data_new[(data_new['vat_li'] > -1) & (data_new['hoa_hoc'] > -1)  & (data_new['sinh_hoc'] > -1 )]
sohstn = loc_TN.count()['sbd']
loc_XH = data_new[(data_new['dia_li'] > -1) & (data_new['gdcd'] > -1) & (data_new['lich_su'] > -1)]
sohsxh = loc_XH.count()['sbd']
# Tính phần trăm số học sinh cho từng môn
total_TNN = sum([(sohstn / Tong )*100])
total_XHH = sum([(sohsxh / Tong)*100 ])

# Vẽ biểu đồ tròn
plt.pie([total_TNN, total_XHH], labels=['Tự nhiên', 'Xã hội'],autopct='%1.1f%%',startangle = 90)
plt.legend(['TỰ NHIÊN','XÃ HỘI'])
plt.title('Phần trăm thí sinh theo tổ hợp tự nhiên và xã hội của 5 tỉnh')
plt.show()


#biểu đồ tròn: phần trăm thí sinh của hai khối tự nhiên và xã hội(5 biểu đồ)
fig, axs = plt.subplots(3, 2, figsize=(13, 13)) #thiết lập vị trí biểu đồ
#lọc những thí sinh tham gia mỗi tổ hợp của tỉnh 50
loc_TN1 = data_tinh1[(data_tinh1['vat_li'] > -1) & (data_tinh1['hoa_hoc'] > -1) & (data_tinh1['sinh_hoc'] > -1)]
sohstn1 = loc_TN1.count()['sbd']
loc_XH1 = data_tinh1[(data_tinh1['dia_li'] > -1) & (data_tinh1['gdcd'] > -1) & (data_tinh1['lich_su'] > -1)]
sohsxh1 = loc_XH1.count()['sbd']
total_TNN1 = sum([(sohstn1 / tinh1 )*100])
total_XHH1 = sum([(sohsxh1 / tinh1 )*100])
# Vẽ biểu đồ tròn và đặt tiêu đề
axs[0, 0].pie([total_TNN1, total_XHH1], labels=['Tự nhiên', 'Xã hội'], autopct='%1.1f%%', startangle=90)
#Thuộc tính bbox_to_anchor=(1, 0.5) cho biết vị trí của legend sẽ được đặt ở bên phải (1) và giữa theo chiều dọc (0.5)
legend = axs[0, 0].legend(['TỰ NHIÊN', 'XÃ HỘI'], bbox_to_anchor=(1, 0.3), loc='upper left')
axs[0, 0].add_artist(legend)
axs[0, 0].set_title('Phần trăm thí sinh thuộc khối tự nhiên và xã hội của tỉnh ĐỒNG THÁP')

#lọc những thí sinh tham gia mỗi tổ hợp của tỉnh 51
loc_TN2 = data_tinh2[(data_tinh2['vat_li'] > -1) & (data_tinh2['hoa_hoc'] > -1) & (data_tinh2['sinh_hoc'] > -1)]
sohstn2 = loc_TN2.count()['sbd']
loc_XH2 = data_tinh2[(data_tinh2['dia_li'] > -1) & (data_tinh2['gdcd'] > -1) & (data_tinh2['lich_su'] > -1)]
sohsxh2 = loc_TN2.count()['sbd']
total_TNN2 = sum([(sohstn2 / tinh2 )*100])
total_XHH2 = sum([(sohsxh2 / tinh2 )*100])
# Vẽ biểu đồ tròn và đặt tiêu đề
axs[0, 1].pie([total_TNN2, total_XHH2], labels=['Tự nhiên', 'Xã hội'], autopct='%1.1f%%', startangle=90)
axs[0, 1].set_title('Phần trăm thí sinh thuộc khối tự nhiên và xã hội tỉnh AN GIANG')

#lọc những thí sinh tham gia mỗi tổ hợp của tỉnh 52
loc_TN3 = data_tinh3[(data_tinh3['vat_li'] > -1) & (data_tinh3['hoa_hoc'] > -1) & (data_tinh3['sinh_hoc'] > -1)]
sohstn3 = loc_TN3.count()['sbd']
loc_XH3 = data_tinh3[(data_tinh3['dia_li'] > -1) & (data_tinh3['gdcd'] > -1) & (data_tinh3['lich_su'] > -1)]
sohsxh3 = loc_XH3.count()['sbd']
total_TNN3 = sum([(sohstn3 / tinh3 )*100])
total_XHH3 = sum([(sohsxh3 / tinh3 )*100])
# Vẽ biểu đồ tròn và đặt tiêu đề
axs[1, 0].pie([total_TNN3, total_XHH3], labels=['Tự nhiên', 'Xã hội'], autopct='%1.1f%%', startangle=90)
axs[1, 0].set_title('Phần trăm thí sinh thuộc khối tự nhiên và xã hội tỉnh BRVT')

#lọc những thí sinh tham gia mỗi tổ hợp của tỉnh 53
loc_TN4 = data_tinh4[(data_tinh4['vat_li'] > -1) & (data_tinh4['hoa_hoc'] > -1) & (data_tinh4['sinh_hoc'] > -1)]
sohstn4 = loc_TN4.count()['sbd']
loc_XH4 = data_tinh4[(data_tinh4['dia_li'] > -1) & (data_tinh4['gdcd'] > -1) & (data_tinh4['lich_su'] > -1)]
sohsxh4 = loc_XH4.count()['sbd']
total_TNN4 = sum([(sohstn4 / tinh4 )*100])
total_XHH4 = sum([(sohsxh4 / tinh4 )*100])
# Vẽ biểu đồ tròn và đặt tiêu đề
axs[1, 1].pie([total_TNN4, total_XHH4], labels=['Tự nhiên', 'Xã hội'], autopct='%1.1f%%', startangle=90)
axs[1, 1].set_title('Phần trăm thí sinh thuộc khối tự nhiên và xã hội tỉnh TIỀN GIANG')

#lọc những thí sinh tham gia mỗi tổ hợp của tỉnh 54
loc_TN5 = data_tinh5[(data_tinh5['vat_li'] > -1) & (data_tinh5['hoa_hoc'] > -1) & (data_tinh5['sinh_hoc'] > -1)]
sohstn5 = loc_TN5.count()['sbd']
loc_XH5 = data_tinh5[(data_tinh5['dia_li'] > -1) & (data_tinh5['gdcd'] > -1) & (data_tinh5['lich_su'] > -1)]
sohsxh5 = loc_XH5.count()['sbd']
total_TNN5 = sum([(sohstn5 / tinh5 )*100])
total_XHH5 = sum([(sohsxh5 / tinh5 )*100])
# Vẽ biểu đồ tròn và đặt tiêu đề
axs[2, 1].pie([total_TNN5, total_XHH5], labels=['Tự nhiên', 'Xã hội'], autopct='%1.1f%%', startangle=90)
axs[2, 1].set_title('Phần trăm điểm tự nhiên và xã hội của các môn tỉnh KIÊN GIANG')

axs[2,0].axis('off')
plt.tight_layout()
plt.show()

#dữ liệu điểm trung bình từng môn của các tỉnh 
#tỉnh 1
DTB_TN1a = loc_TN1['sinh_hoc'].mean()
DTB_TN1b = loc_TN1['vat_li'].mean()
DTB_TN1c = loc_TN1['hoa_hoc'].mean()
DTB_XH1a = loc_XH1['lich_su'].mean()
DTB_XH1b = loc_XH1['dia_li'].mean()
DTB_XH1c = loc_XH1['gdcd'].mean()
#tỉnh 2
DTB_TN2a = loc_TN2['sinh_hoc'].mean()
DTB_TN2b = loc_TN2['vat_li'].mean()
DTB_TN2c = loc_TN2['hoa_hoc'].mean()
DTB_XH2a = loc_XH2['lich_su'].mean()
DTB_XH2b = loc_XH2['dia_li'].mean()
DTB_XH2c = loc_XH2['gdcd'].mean()
#tỉnh 3
DTB_TN3a = loc_TN3['sinh_hoc'].mean()
DTB_TN3b = loc_TN3['vat_li'].mean()
DTB_TN3c = loc_TN3['hoa_hoc'].mean()
DTB_XH3a = loc_XH3['lich_su'].mean()
DTB_XH3b = loc_XH3['dia_li'].mean()
DTB_XH3c = loc_XH3['gdcd'].mean()
#tỉnh 4
DTB_TN4a = loc_TN4['sinh_hoc'].mean()
DTB_TN4b = loc_TN4['vat_li'].mean()
DTB_TN4c = loc_TN4['hoa_hoc'].mean()
DTB_XH4a = loc_XH4['lich_su'].mean()
DTB_XH4b = loc_XH4['dia_li'].mean()
DTB_XH4c = loc_XH4['gdcd'].mean()
#tỉnh 5
DTB_TN5a = loc_TN5['sinh_hoc'].mean()
DTB_TN5b = loc_TN5['vat_li'].mean()
DTB_TN5c = loc_TN5['hoa_hoc'].mean()
DTB_XH5a = loc_XH5['lich_su'].mean()
DTB_XH5b = loc_XH5['dia_li'].mean()
DTB_XH5c = loc_XH5['gdcd'].mean()

#dữ liệu điểm trung bình mỗi tổ hợp của các tỉnh
categories = ['Đồng Tháp', 'An Giang', 'Bà Rịa', 'Tiền Giang', 'Kiên Giang']
total_TNN1 = sum([(DTB_TN1a + DTB_TN1b + DTB_TN1c)/ 3] )
total_XHH1 = sum([(DTB_XH1a + DTB_XH1b + DTB_XH1c)/ 3])
total_TNN2 = sum([(DTB_TN2a + DTB_TN2b + DTB_TN2c)/ 3] )
total_XHH2 = sum([(DTB_XH2a + DTB_XH2b + DTB_XH2c)/ 3 ])
total_TNN3 = sum([(DTB_TN3a + DTB_TN3b + DTB_TN3c)/ 3 ])
total_XHH3 = sum([(DTB_XH3a + DTB_XH3b + DTB_XH3c)/ 3 ])
total_TNN4 = sum([(DTB_TN4a + DTB_TN4b + DTB_TN4c)/ 3 ])
total_XHH4 = sum([(DTB_XH4a + DTB_XH4b + DTB_XH4c)/ 3 ])
total_TNN5 = sum([(DTB_TN5a + DTB_TN5b + DTB_TN5c)/ 3 ])
total_XHH5 = sum([(DTB_XH5a + DTB_XH5b + DTB_XH5c)/ 3]) 
values1 = [total_TNN1, total_TNN2, total_TNN3, total_TNN4, total_TNN5 ]
values2 = [total_XHH1, total_XHH2, total_XHH3, total_XHH4, total_XHH5]

x = range(len(categories))  # Vị trí của các cột
width = 0.35  # Độ rộng của cột

# Vẽ biểu đồ
fig, ax = plt.subplots()
bars1 = ax.bar([i - width/2 for i in x], values1, width, label='Tự nhiên')
bars2 = ax.bar([i + width/2 for i in x], values2, width, label='Xã hội')
# Đặt các nhãn và tiêu đề
ax.set_xlabel('Tỉnh')
ax.set_ylabel('Điểm Trung Bình')
ax.set_title('Biểu đồ Điểm Trung Bình Giữa Hai Khối Tự Nhiên và Xã Hội')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend(bbox_to_anchor=(1, 0.5))
for bar1, bar2 in zip(bars1, bars2):
    yval1 = bar1.get_height()
    yval2 = bar2.get_height()
    plt.text(bar1.get_x() + bar1.get_width()/2, yval1 + 0.05, round(yval1, 2), ha='center', va='bottom')
    plt.text(bar2.get_x() + bar2.get_width()/2, yval2 + 0.05, round(yval2, 2), ha='center', va='bottom')
# Hiển thị biểu đồ
plt.show()

#Thống kê điểm cao và điểm thấp
# Tính tổng điểm bài thi tổ hợp tự nhiên của mỗi học sinh
loc_TN['Total'] = loc_TN[['vat_li', 'hoa_hoc','sinh_hoc']].sum(axis=1) 
# Sắp xếp dữ liệu theo cột Total (tổng điểm) để tìm 5 học sinh có điểm cao nhất và thấp nhất của mỗi khối
top_students = loc_TN.nlargest(5, 'Total')  # Tìm 5 học sinh có điểm cao nhất
bottom_students = loc_TN.nsmallest(5, 'Total')  # Tìm 5 học sinh có điểm thấp nhất
print("5 học sinh có điểm cao nhất trong khối tự nhiên là:")
print(top_students)
print("\n5 học sinh có điểm thấp nhất trong khối tự nhiên là:")
print(bottom_students)

# Tính tổng điểm bài thi tổ hợp xã hội của mỗi học sinh
loc_XH['Total'] = loc_XH[['lich_su', 'dia_li','gdcd']].sum(axis=1) 
# Sắp xếp dữ liệu theo cột Total (tổng điểm) để tìm 5 học sinh có điểm cao nhất và thấp nhất
top_students = loc_XH.nlargest(5, 'Total')  # Tìm 5 học sinh có điểm cao nhất
bottom_students = loc_XH.nsmallest(5, 'Total')  # Tìm 5 học sinh có điểm thấp nhất
print("5 học sinh có điểm cao nhất trong khối xã hội là:")
print(top_students)
print("\n5 học sinh có điểm thấp nhất trong khối xã hội là:")
print(bottom_students)

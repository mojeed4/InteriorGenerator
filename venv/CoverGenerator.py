from fpdf import FPDF
from SizeCalculator import SizeCalculator as SC

new_page = SC((6,9), 110, 1)
print(new_page.get_spine_size())
print(new_page.get_cover_size())

pdf = FPDF('P', 'in', new_page.get_cover_size())
pdf.add_page()
pdf.set_fill_color(248, 170, 143)
print(new_page.get_cover_width())
pdf.rect(0, 0, new_page.get_cover_width(), new_page.get_cover_height(), 'F')
pdf.set_fill_color(255, 255, 255)
pdf.rect(0.25, 0.25, new_page.get_trim_width()-0.25, new_page.get_trim_height()-0.25, 'F')

start_x = 0.0625 + 0.125 + new_page.get_trim_width()
pdf.rect(start_x, 0.25, new_page.get_spine_size() - (2 * 0.0625), new_page.get_trim_height()-0.25, 'F')

start_x = 0.25 + new_page.get_trim_width() + new_page.get_spine_size()
pdf.rect(start_x, 0.25, new_page.get_trim_width()-0.25, new_page.get_trim_height()-0.25, 'F')

#left vertical line
pdf.dashed_line(0.125, 0.125, 0.125, new_page.get_trim_height()+0.125, 0.05, 0.05)

#Right vertical line
start_x = new_page.get_cover_width() - 0.125
pdf.dashed_line(start_x, 0.125, start_x, new_page.get_trim_height()+0.125, 0.05, 0.05)

#Top horizontal line
pdf.dashed_line(0.125, 0.125, start_x, 0.125, 0.05, 0.05)

#Bottom horizontal line
start_y = new_page.get_cover_height() - 0.125
pdf.dashed_line(0.125, start_y, start_x, start_y, 0.05, 0.05)

#Spine vertical lines
start_x = 0.125 + new_page.get_trim_width()
print('start x', start_x)
pdf.dashed_line(start_x, 0, start_x, new_page.get_trim_height()+0.25, 0.05, 0.05)
start_x = new_page.get_cover_width() - (new_page.get_trim_width() + 0.125)
print('start x', start_x)
pdf.dashed_line(start_x, 0, start_x, new_page.get_trim_height()+0.25, 0.05, 0.05)

pdf.set_font('helvetica', 'B', 25)
start_x = 0.25 + new_page.get_trim_width()
pdf.cell(start_x, new_page.get_trim_height()-1, '             Created by Majid!', 'C')
pdf.output('Cover Irregular.pdf')


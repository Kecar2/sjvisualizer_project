from sjvisualizer import BarRace
from sjvisualizer import PieRace
from sjvisualizer import DataHandler
from sjvisualizer import Canvas
from sjvisualizer import StaticImage

file_name = 'data/datos_transpuestos.xlsx'
fps = 60
duration = 0.8

df = DataHandler.DataHandler(
    excel_file=file_name, number_of_frames=fps*duration*60).df

canvas = Canvas.canvas()

bar_chart = BarRace.bar_race(df=df, canvas=canvas.canvas)
canvas.add_sub_plot(bar_chart)

# Crear el gráfico de pie
pie_chart = PieRace.pie_plot(canvas=canvas.canvas, df=df, display_percentages=False, display_label=False, x_pos=1300, y_pos=600, height=250, width=500)
canvas.add_sub_plot(pie_chart)  # Ajusta las coordenadas según tus necesidades

ex = StaticImage.static_image(
    canvas=canvas.canvas, file="assets/alimentos.png", x_pos=380, y_pos=20, width=115, height=115)
canvas.add_sub_plot(ex)

# adding decoration with TkInter
line = canvas.canvas.create_line(
    500, 40, 500, 150, width=10, fill=Canvas._from_rgb((75, 75, 155)))


canvas.add_title("Inflación de los precios de los alimentos", color=(0, 0, 0))
canvas.add_sub_title(
    "2008 - 2023 | Valor en % | 25 paises", color=(150, 150, 150))

# adding a time
canvas.add_time(df=df, time_indicator="year")

# adding a logo
canvas.add_logo(logo="logoVletraN.png")

# play the animation
canvas.play()

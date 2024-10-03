from tkinter import *
from PIL import Image,ImageTk
import webbrowser

###############  FUNCIONES  #################
def linkIA ():
    webbrowser.open('https://poe.com/ODS_IA')

def Pobreza():
    ventanap=Toplevel(ventana)
    ventanap.title("Fin de la Pobreza")
    ventanap.config(bg="#E5233B")
    ventanap.geometry("830x600")
    ventanap.iconbitmap('pensionado.ico')
    ventanap.resizable(0,0)
     
    lbltitulop=Label(ventanap,text='Fin de la Pobreza',background='#E5233B',font=('Arial',22,'bold')).place(x=90,y=20)

    texto=Text(ventanap, height=28, width=52,background='#E5233B')
    texto.place(x=25, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'El ODS 1 busca erradicar la pobreza en todas sus\n'
                 'formas hasta 2030, para lograr esto se enfoca en\n'
                 'casos de pobreza extrema.\n\n' 
                 'Desde la década de los 90´s se ha logrado reducir\n' 
                 'la cantidad de pobreza extrema con relativo éxito,\n' 
                 'pero hoy en día 1 de cada 5 personas aún sigue\n'
                 'subsistiendo con menos de $1,25 al día.\n\n'
                 'La Organización de las Naciones Unidas(ONU) nos\n'
                 'dice que las razones por las que existe la pobreza\n'
                 'en el mundo son el desempleo, la discriminación y la\n'
                 'vulnerabilidad ante los desastres naturales y las\n' 
                 'enfermedades.\n\n'
                 'La pobreza no solo se trata de la falta de ingresos,\n'
                 'también incluye la malnutrición, la discriminación,\n'
                 'la fata de servicios básicos, la falta de educación\n'
                 'y la exposición a climas extremos.\n\n'
                 'En Ecuador se ha podido desvincular a 3.816 niños\n'
                 'deltrabajo infantil, 10.515 jóvenes fueron educados \n'
                 'para la inclusíon económica juvenil; además, la \n'
                 'pobreza multidimensional disminuyó 2,71 puntos.','blancodos')
    texto.config(state=DISABLED)
    
    texto=Text(ventanap, height=23, width=44,background='#E5233B')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'1.1: Erradicar la pobreza extrema en todo el\n' 
                 'mundo hasta 2030.\n\n'
                 '1.1.1: Medir y vigilar el umbral de pobreza\n' 
                 'extrema, por sexo, edad, situación laboral y\n'
                 'zona geográfica.\n\n'
                 '1.2: Reducir por lo menos a la mitad la\n' 
                 'cantidad de personas que viven en la pobreza\n\n'
                 '1.2.1: Conocer la cantidad de personas que\n'
                 'vive bajo el umbral de pobreza, desglosada\n'
                 'por edad y sexo.\n\n'
                 '1.2.2: Saber la cantidad de personas pobres\n'
                 'según definiciones nacionales.\n\n'
                 '1.3: Implementar medidas de protección para\n'
                 'todos hasta 2030, así logrando obtener una\n'
                 'cobertura de las personas pobres.\n\n'
                 '1.3.1: Conocer el porcentage de cobertura\n'
                 'de protección social, desglosado por sexo,\n'
                 'edad, mujeres embarazadas, desempleados,\n\n'
                 'víctimas de accidentes y grupos vulnerables.\n\n'
                 '1.4: Garantizar los derechos a recursos\n'
                 'económicos y servicios básicos.\n\n'
                 '1.4.1: Conocer la cantidad de personas con\n'
                 'acceso a servicios básicos.\n\n'
                 '1.5: Fomentar la resiliencia de los pobres\n'
                 'que se encuentran en situaciones vulnerables\n'
                 'y expuestos a condiciones climáticas.\n\n'
                 '1.5.1: Conocer el número de muertos, heridos\n'
                 'desaparecidos, reubicados y evacuados por\n'
                 'cada 100.000 personas.\n\n'
                 '1.a: Garantizar la movilización de recursos\n'
                 'para que las naciones en desarrollo apliquen\n'
                 'programas y políticas para poner fin a la\n'
                 'pobreza en todas sus dimensiones.\n\n'
                 '1.a.1: Conocer la cantidad de recursos que\n'
                 'se han asignado a reducir la pobreza\n\n'
                 '1.b: Crear marcos normativos sobre la base\n'
                 'de estrategias de desarrollo en favor de los\n'
                 'pobres, tomando en cuenta género y edad.\n\n'
                 '1.b.1: Saber el número de planes nacionales\n'
                 'relacionados con acuerdos ambientales que\n'
                 'apoyen la inversión acelerada para erradicar\n'
                 'la pobreza.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://view.genially.com/66eca552583fcf0aaf05180b/interactive-content-ods-1')
    
    btnlink=Button(ventanap,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    salirp=ventanap.destroy
    btnsalirp=Button(ventanap,text='Volver',font=('Arial',14,'bold'),foreground='red',command=salirp).place(x=725,y=550)

    a=Image.open('ods1.png')
    a=a.resize((250,130))
    a=ImageTk.PhotoImage(a) 
    lblimg=Label(ventanap,image=a,border=0).place(x=500,y=20)
    lblimg.pack()
    lblimg.image=a

def Hambre():
    ventanah=Toplevel(ventana)
    ventanah.title("Hambre Cero")
    ventanah.config(bg="#D29F28")
    ventanah.geometry("830x600")
    ventanah.iconbitmap('pensionado.ico')
    ventanah.resizable(0,0)

    lbltituloh=Label(ventanah,text='Hambre Cero',background='#D29F28',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanah, height=28, width=52,background='#D29F28')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'El objetivo 2 es crear un mundo libre de hambre para\n' 
                 '2030. El problema global del hambre y la inseguridad\n' 
                 'alimentaria ha mostrado un aumento alarmante desde\n' 
                 '2015, una tendencia exacerbada por una combinación\n' 
                 'de factores que como la pandemia, los conflictos,\n' 
                 'el cambio climático y la profundización de las\n' 
                 'desigualdades.\n\n'
                 'En 2022, aproximadamente 735 millones de personas\n' 
                 '(o el 9,2 % de la población mundial) se encontraban\n' 
                 'en estado de hambre crónica, un aumento vertiginoso\n' 
                 'en comparación con 2019. Estos datos subrayan la\n' 
                 'gravedad de la situación y revelan una crisis\n'
                 'creciente.\n\n'
                 'El hambre no solo afecta a la salud y bienestar de\n'
                 'las personas sino que tambien diminuye en gran\n' 
                 'medida su productividad lo que hace que la economía\n'
                 'no pueda desarrollarce de forma correcta aumentando\n'
                 'en índice de pobreza diezmando el progreso que de\n'
                 'la ODS 1.\n\n'
                 'Para la correcta realización de esta ODS se debe\n'
                 'promover la agrucultura sostenible para asi poder\n'
                 'brindar suficiente alimento a todas las personas.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanah, height=23, width=44,background='#D29F28')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'2.1 Para 2030, eliminar toda el hambre y\n' 
                 'garantizar que todas las personas,\n' 
                 'especialmente los pobres y los vulnerables\n' 
                 'tengan acceso a una alimentación sana.\n'
                 '2.2 Para 2030, erradicar todas las formas de\n' 
                 'malnutrición, logrando para 2025 las metas\n' 
                 'internacionales sobre el retraso del\n' 
                 'crecimiento y la emaciación en los niños\n' 
                 'menores de 5 años.\n'
                 '2.3 Para 2030, duplicar la productividad\n' 
                 'agrícola y los ingresos de los pequeños\n' 
                 'productores de alimentos, especialmente\n' 
                 'mujeres, pueblos indígenas, agricultores\n' 
                 'familiares, pastores y pescadores,\n' 
                 'facilitando su acceso equitativo a tierras,\n' 
                 'insumos, recursos, conocimientos, servicios\n' 
                 'financieros, mercados y oportunidades de\n' 
                 'empleo no agrícola.\n'
                 '2.4 Para 2030, asegurar la sostenibilidad de\n' 
                 'los sistemas de producción de alimentos y\n' 
                 'promover prácticas agrícolas resilientes que\n' 
                 'incrementen la productividad y mantengan los\n' 
                 'ecosistemas.\n'
                 '2.5 Para 2020, preservar la diversidad\n'
                 'genética de las semillas, plantas cultivadas\n' 
                 'y animales de granja, y especies silvestres\n' 
                 'relacionadas, mediante la gestión y\n' 
                 'diversificación de bancos de semillas y\n' 
                 'plantas a nivel nacional.\n'
                 '2.a Aumentar las inversiones, incluyendo la\n' 
                 'cooperación internacional, infraestructura\n' 
                 'rural, investigación agrícola, servicios de\n' 
                 'extensión y desarrollo tecnológico.\n'
                 '2.b Corregir y prevenir las distorsiones y\n' 
                 'restricciones comerciales en los mercados\n' 
                 'agropecuarios mundiales.\n'
                 '2.c Tomar medidas para garantizar el\n' 
                 'correcto funcionamiento de los mercados de\n' 
                 'productos alimentarios y facilitar el\n' 
                 'acceso a información oportuna sobre los\n' 
                 'mercados.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://view.genially.com/66f995d35a234af623b22eae/interactive-content-ods-2')

    btnlink=Button(ventanah,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    salirh=ventanah.destroy
    btnsalirh=Button(ventanah,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirh).place(x=725,y=550)

    a=Image.open('ods2.png')
    a=a.resize((130,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanah,image=a,border=0).place(x=550,y=20)
    lblholah.pack()
    lblholah.image=a

def Salud():
    ventanas=Toplevel()
    ventanas.title("Buena Salud")
    ventanas.config(bg="#269B48")
    ventanas.geometry("830x600")
    ventanas.iconbitmap('pensionado.ico')
    ventanas.resizable(0,0)

    lbltitulos=Label(ventanas,text='Buena Salud',background='#269B48',font=('Arial',14,'bold')).place(x=100,y=20)

    texto=Text(ventanas, height=28, width=52,background='#269B48')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'Garantizar una vida sana y promover el bienestar\n' 
                 'para todos en todas las edades. En los últimos años\n' 
                 'se han logrado grandes avances en la mejora de la\n' 
                 'salud de las personas. 146 de 200 países o regiones\n' 
                 'ya han cumplido o están en camino de alcanzar la\n' 
                 'meta de los ODS sobre mortalidad en menores de 5\n' 
                 'años.\n\n' 
                 'El tratamiento eficaz contra el VIH ha reducido las\n' 
                 'muertes relacionadas con el sida en un 52 % desde\n' 
                 '2010 y se ha eliminado al menos una enfermedad\n' 
                 'tropical desatendida en 47 países.\n\n'
                 'Sin embargo, todavía persisten las desigualdades en\n' 
                 'el acceso a la atención sanitaria. La pandemia de\n' 
                 'la COVID-19 y otras crisis en curso han impedido el\n' 
                 'progreso hacia el objetivo 3.\n\n'
                 'Esta ODS también nos dice que se debe de impulsar\n'
                 'el desarrollo de vacunas y medicamentos de tal modo\n'
                 'que sea accesible para todo el público a un precio\n'
                 'en el que las empresas no pierdan dinero y las\n'
                 'personas puedan comprarlas a buen precio.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanas, height=23, width=44,background='#269B48')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'3.1 Para 2030, disminuir la tasa global de\n' 
                 'mortalidad materna a menos de 70 por cada\n' 
                 '100.000 nacidos vivos.\n'
                 '3.2 Para 2030, poner fin a las muertes\n' 
                 'evitables de recién nacidos y de niños\n' 
                 'menores de 5 años.\n'
                 '3.3 Para 2030, erradicar las epidemias de\n'
                 'SIDA, tuberculosis, malaria y enfermedades\n' 
                 'tropicales desatendidas.\n'
                 '3.4 Para 2030, reducir en un tercio la\n' 
                 'mortalidad prematura por enfermedades no\n' 
                 'transmisibles a través de la prevención y\n' 
                 'el tratamiento.\n'
                 '3.5 Fortalecer la prevención y el\n' 
                 'tratamiento del abuso de sustancias\n' 
                 'adictivas.\n'
                 '3.6 Para 2020, reducir a la mitad el número\n' 
                 'de muertes y lesiones causadas por\n' 
                 'accidentes de tráfico en el mundo.\n'
                 '3.7 Para 2030, asegurar el acceso universal\n' 
                 'a servicios de salud sexual y reproductiva,\n' 
                 'incluyendo planificación familiar,\n' 
                 'información y educación.\n'
                 '3.8 Lograr la cobertura sanitaria universal,\n' 
                 'especialmente la protección contra riesgos\n' 
                 'financieros, acceso a servicios de salud\n' 
                 'esenciales de calidad.\n'
                 '3.9 Para 2030, reducir de manera\n' 
                 'significativa el número de muertes y\n' 
                 'enfermedades causadas por productos químicos\n' 
                 'peligrosos.\n'
                 '3.a Reforzar la implementación del Convenio\n' 
                 'Marco de la OMS para el Control del Tabaco\n' 
                 'en todos los países, según corresponda.\n'
                 '3.b Apoyar las actividades de investigación\n' 
                 'y desarrollo de vacunas y medicamentos para\n' 
                 'enfermedades transmisibles y no\n' 
                 'transmisibles que afectan principalmente a\n' 
                 'los países en desarrollo, facilitando el\n' 
                 'acceso a medicamentos y vacunas esenciales\n' 
                 'asequibles.\n'
                 '3.c Aumentar considerablemente la\n' 
                 'financiación en salud y la contratación,\n' 
                 'desarrollo, capacitación y retención del\n' 
                 'personal sanitario en países en desarrollo.\n'
                 '3.d Fortalecer la capacidad de todos los\n' 
                 'países,en cuanto a alerta temprana,\n' 
                 'reducción de riesgos y gestión de riesgos\n' 
                 'para la salud nacional y global.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://view.genially.com/66f9a1eacb53193c9a82b167/interactive-content-ods-3')
    
    btnlink=Button(ventanas,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    salirs=ventanas.destroy
    btnsalirs=Button(ventanas,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirs).place(x=725,y=550)

    a=Image.open('ods3.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanas,image=a,border=0).place(x=600,y=20)
    lblholah.pack()
    lblholah.image=a

def Educacion():
    ventanae=Toplevel()
    ventanae.title("Educación de Calidad")
    ventanae.config(bg="#CB1A2A")
    ventanae.geometry("830x600")
    ventanae.iconbitmap('pensionado.ico')
    ventanae.resizable(0,0)

    lbltituloe=Label(ventanae,text='Educación de Calidad',background='#CB1A2A',font=('Arial',14,'bold')).place(x=100,y=20)

    texto=Text(ventanae, height=28, width=52,background='#CB1A2A')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'Garantizar una educación inclusiva, equitativa y de\n' 
                 'calidad y promover oportunidades de aprendizaje\n' 
                 'durante toda la vida para todos.\n\n'
                 'El progreso hacia una educación de calidad ya era\n' 
                 'más lento de lo requerido antes de la pandemia, pero\n' 
                 'la COVID-19 ha tenido impactos devastadores en la\n' 
                 'educación, provocando pérdidas de aprendizaje en\n' 
                 'cuatro de cada cinco países de un total de 104\n' 
                 'analizados.\n\n'
                 'Sin medidas adicionales, se estima que 84 millones\n' 
                 'de niños y jóvenes no asistirán a la escuela de aquí\n' 
                 'a 2030 y aproximadamente 300 millones de estudiantes\n'
                 'carecerán de las habilidades básicas de aritmética y\n' 
                 'alfabetización necesarias para tener éxito.\n\n'
                 'El progreso hacia una educación de calidad ya era\n' 
                 'más lento de lo requerido antes de la pandemia, pero\n' 
                 'la covid-19 ha tenido impactos devastadores en la\n' 
                 'educación, provocando pérdidas de aprendizaje en\n' 
                 'cuatro de cada cinco países de un total de 104\n' 
                 'analizados.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanae, height=23, width=44,background='#CB1A2A')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'4.1 Para 2030, garantizar que todas las\n' 
                 'niñas y niños completen la educación\n' 
                 'primaria y secundaria, la cual debe ser\n' 
                 'gratuita, equitativa y de calidad.\n'
                 '4.2 Para 2030, asegurar que todas las niñas\n' 
                 'y niños tengan acceso a servicios de\n' 
                 'atención y desarrollo en la primera\n' 
                 'infancia.\n'
                 '4.3 Para 2030, garantizar el acceso\n' 
                 'equitativo de hombres y mujeres a formación\n' 
                 'técnica, profesional y superior de calidad,\n' 
                 'incluyendo la educación universitaria.\n'
                 '4.4 Para 2030, aumentar significativamente\n' 
                 'el número de jóvenes y adultos que poseen\n' 
                 'las competencias necesarias, especialmente\n' 
                 'técnicas y profesionales, para acceder a\n' 
                 'empleo, trabajo decente y emprendimiento.\n'
                 '4.5 Para 2030, eliminar las disparidades\n' 
                 'de género en la educación y asegurar el\n' 
                 'acceso equitativo a todos los niveles de\n' 
                 'enseñanza y formación profesional para\n' 
                 'personas vulnerables.\n'
                 '4.6 Para 2030, garantizar que todos los\n' 
                 'jóvenes y una proporción significativa de\n' 
                 'adultos, tanto hombres como mujeres, sean\n' 
                 'alfabetizados y tengan conocimientos\n' 
                 'básicos de aritmética.\n'
                 '4.7 Para 2030, asegurar que todos los\n' 
                 'alumnos adquieran los conocimientos\n' 
                 'teóricos y prácticos necesarios para\n' 
                 'promover el desarrollo sostenible.\n'
                 '4.a Construir y adecuar instalaciones\n' 
                 'educativas que consideren las necesidades\n' 
                 'de los niños y personas con discapacidad.\n'
                 '4.b Para 2020, aumentar considerablemente\n' 
                 'el número de becas disponibles a nivel\n' 
                 'mundial para los países en desarrollo\n'
                 '4.c Para 2030, aumentar significativamente\n' 
                 'la cantidad de docentes calificados, incluso\n' 
                 'a través de la cooperación internacional en\n' 
                 'la formación de maestros en los países en\n' 
                 'desarrollo.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://wordwall.net/es/resource/36890165/educaci%C3%B3n-de-calidad')
    
    btnlink=Button(ventanae,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    salire=ventanae.destroy
    btnsalire=Button(ventanae,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salire).place(x=725,y=550)

    a=Image.open('ods4.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanae,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Igualdad():
    ventanai=Toplevel()
    ventanai.title("Igualdad de género")
    ventanai.config(bg="#FF3A20")
    ventanai.geometry("830x600")
    ventanai.iconbitmap('pensionado.ico')
    ventanai.resizable(0,0)

    lbltituloi=Label(ventanai,text='Igualdad de Género',background='#FF3A20',font=('Arial',14,'bold')).place(x=100,y=20)

    texto=Text(ventanai, height=28, width=52,background='#FF3A20')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'Lograr la igualdad entre los géneros y empoderar a\n' 
                 'todas las mujeres y las niñas. La igualdad de género\n' 
                 'no solo es un derecho humano fundamental, sino que\n' 
                 'es uno de los fundamentos esenciales para construir\n' 
                 'un mundo pacífico, próspero y sostenible.\n\n' 
                 'Se han conseguido algunos avances en las últimas\n' 
                 'décadas, pero el mundo está lejos de alcanzar la\n' 
                 'igualdad de género para 2030.\n\n'
                 'Las mujeres y niñas constituyen la mitad de la\n' 
                 'población mundial y, por tanto, también la mitad de\n' 
                 'su potencial.\n\n'
                 'En esta ODS también se incluye la reducción de la\n'
                 'brecha salarial y el acceso de todas la niñas y\n' 
                 'mujeres a la salud reproductiva y sexual; además de\n'
                 'la eliminación de discriminación y violencia hacia\n'
                 'la mujer.\n\n'
                 'Para el cumplimiento de esta ODS se debe reconocer\n'
                 'los aportes de las mujeres en lo económico, social\n'
                 'y moral.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanai, height=23, width=44,background='#FF3A20')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'5.1 Erradicar todas las formas existentes de\n' 
                 'discriminación contra todas las mujeres y\n' 
                 'niñas en todo el mundo.\n'
                 '5.2 Eliminar todas las formas de violencia\n' 
                 'contra mujeres y niñas en los ámbitos\n' 
                 'público y privado, incluyendo la trata, la\n' 
                 'explotación sexual y otras formas de\n' 
                 'explotación.\n'
                 '5.3 Erradicar todas las prácticas\n' 
                 'perjudiciales, como el matrimonio infantil,\n' 
                 'precoz y forzado, así como la mutilación\n' 
                 'genital femenina.\n'
                 '5.4 Reconocer y valorar el trabajo de\n' 
                 'cuidado y doméstico no remunerado mediante\n' 
                 'servicios públicos, infraestructura y\n' 
                 'políticas de protección social.\n'
                 '5.5 Garantizar la participación plena y\n' 
                 'efectiva de las mujeres y la igualdad de\n' 
                 'oportunidades de liderazgo en todos los\n' 
                 'niveles.\n'
                 '5.6 Asegurar el acceso universal a la salud\n' 
                 'sexual y reproductiva y los derechos\n' 
                 'reproductivos.\n'
                 '5.a Implementar reformas que otorguen a las\n' 
                 'mujeres igualdad de derechos sobre recursos\n' 
                 'económicos, así como acceso a la propiedad\n' 
                 'y control de la tierra y otros bienes.\n'
                 '5.b Mejorar el uso de tecnologías,\n' 
                 'especialmente la tecnología de la\n' 
                 'información y las comunicaciones.\n'
                 '5.c Adoptar y fortalecer políticas y leyes\n' 
                 'efectivas para promover la igualdad de\n' 
                 'género.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://wordwall.net/resource/69687214/ods-5-igualdad-de-g%C3%A9nero')
    
    btnlink=Button(ventanai,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    saliri=ventanai.destroy
    btnsaliri=Button(ventanai,text='Volver',font=('Arial',12,'bold'),foreground='red',command=saliri).place(x=725,y=550)

    a=Image.open('ods5.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanai,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Agua():
    ventanaa=Toplevel()
    ventanaa.title("Agua limpia y Saneamiento")
    ventanaa.config(bg="#00ACD8")
    ventanaa.geometry("830x600")
    ventanaa.iconbitmap('pensionado.ico')
    ventanaa.resizable(0,0)

    lbltituloa=Label(ventanaa,text='Agua Limpia y Saneamiento',background='#00ACD8',font=('Arial',14,'bold')).place(x=100,y=20)

    texto=Text(ventanaa, height=28, width=52,background='#00ACD8')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'El acceso a agua potable, saneamiento e higiene es\n' 
                 'una necesidad fundamental para la salud y el\n' 
                 'bienestar humano. Hasta hoy, miles de millones de\n' 
                 'personas siguen sin contar con estos servicios\n' 
                 'esenciales.\n\n' 
                 'El incremento poblacional, la urbanización y la\n' 
                 'creciente demanda de agua en sectores como la\n' 
                 'agricultura, industria y energía están generando\n' 
                 'una mayor presión sobre los recursos hídricos.\n'
                 'se debe llegar a una repartición equitativa y\n'
                 'universal de agua potable a un precio adecuado\n'
                 'para todas las personas; además se debe reducir\n'
                 'al mímino la emisión de sustancias dañinas en las\n'
                 'fuentes hídricas de cada nación.\n\n'
                 'El acceso al agua es una prioridad ya que no solo\n'
                 'contribuye a la salud sino que tambien ayuda a\n'
                 'mejorar la productividad de todas las personas lo\n'
                 'que mejora la economía de las familias y naciones\n'
                 'a la vez.\n\n'
                 'Para lograr esto se debe realizar una mejora en la\n'
                 'infraestructura de las instalaciones sanitarias y\n'
                 'distribuidoras de agua.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanaa, height=23, width=44,background='#00ACD8')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'6.1 Para 2030, asegurar que todas las\n' 
                 'personas tengan acceso universal y\n' 
                 'equitativo a agua potable a un costo\n' 
                 'accesible.\n'
                 '6.2 Para 2030, garantizar que todos cuenten\n' 
                 'con servicios adecuados y equitativos de\n' 
                 'saneamiento e higiene, erradicando la\n' 
                 'defecación al aire libre, con especial\n' 
                 'atención a las mujeres, niñas y personas en\n' 
                 'situaciones vulnerables.\n'
                 '6.3 Para 2030, mejorar la calidad del agua\n' 
                 'reduciendo la contaminación, eliminando\n' 
                 'vertidos y restringiendo la emisión de\n' 
                 'sustancias peligrosas, disminuyendo a la\n' 
                 'mitad las aguas residuales sin tratar y\n' 
                 'fomentando el reciclaje y la reutilización\n' 
                 'segura del agua a nivel mundial.\n'
                 '6.4 Para 2030, aumentar significativamente\n' 
                 'la eficiencia en el uso del agua en todos\n' 
                 'los sectores, asegurando la sostenibilidad\n' 
                 'en la extracción y suministro de agua dulce\n' 
                 'para enfrentar la escasez y reducir el\n' 
                 'número de personas afectadas por la falta deagua.\n'
                 '6.5 Para 2030, implementar una gestión\n' 
                 'integrada de los recursos hídricos en todos\n' 
                 'los niveles, incluyendo la cooperación\n' 
                 'transfronteriza cuando sea necesario.\n'
                 '6.6 Para 2020, proteger y restaurar los\n' 
                 'ecosistemas vinculados al agua, tales como \n' 
                 'bosques, montañas, humedales, ríos,\n' 
                 'acuíferos y lagos.'
                 '6.a Para 2030, aumentar la cooperación\n.' 
                 'internacional y el apoyo a los países en\n' 
                 'desarrollo en la creación de capacidades\n' 
                 'para programas y actividades relacionadas\n' 
                 'con el agua y el saneamiento, como la\n' 
                 'captación de agua, desalinización, uso\n' 
                 'eficiente de recursos hídricos, tratamiento\n' 
                 'de aguas residuales y tecnologías de\n' 
                 'reutilización.'
                 '6.b Apoyar y fortalecer la participación de\n' 
                 'las comunidades locales en la mejora de la\n' 
                 'gestión del agua y saneamiento.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://wordwall.net/es/resource/5091813/ods-agua-limpia-y-saneamiento')
    
    btnlink=Button(ventanaa,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    salira=ventanaa.destroy
    btnsalira=Button(ventanaa,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salira).place(x=725,y=550)

    a=Image.open('ods6.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanaa,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Energia():
    ventanaen=Toplevel()
    ventanaen.title("Energía Asequible y No Contaminante")
    ventanaen.config(bg="#FEB612")
    ventanaen.geometry("830x600")
    ventanaen.iconbitmap('pensionado.ico')
    ventanaen.resizable(0,0)

    lbltituloen=Label(ventanaen,text='Energía Asequible y No Contaminante',background='#FEB612',font=('Arial',14,'bold')).place(x=100,y=20)

    texto=Text(ventanaen, height=28, width=52,background='#FEB612')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('textos',foreground='black')
    texto.insert(END,'El Objetivo 7 busca asegurar el acceso a una energía\n' 
                 'limpia y asequible, fundamental para el desarrollo\n' 
                 'de sectores como la agricultura, negocios,\n' 
                 'comunicaciones, educación, salud y transporte.\n\n' 
                 'Aunque se han logrado avances hacia la energía\n' 
                 'sostenible, el progreso no es lo suficientemente\n' 
                 'rápido. De mantenerse el ritmo actual, cerca de 660\n' 
                 'millones de personas seguirán sin acceso a \n' 
                 'electricidad y cerca de 2000 millones continuarán\n' 
                 'usando combustibles y tecnologías contaminantes para\n' 
                 'cocinar en 2030.\n\n'
                 'La energía segura y accesible es esencial en nuestra\n' 
                 'vida diaria, pero el consumo energético sigue siendo\n' 
                 'la mayor causa del cambio climático, representando\n' 
                 'alrededor del 60 % de las emisiones globales de\n' 
                 'gases de efecto invernadero.\n\n'
                 'Se debe invertir en fuentes de energíacomo son la\n'
                 'eólica, solar y termal. También se necesita adoptar\n'
                 'estándares ,en función de costos, para reducir el\n'
                 'consumo energético en todo el mundo.','textos')
    texto.config(state=DISABLED)

    texto=Text(ventanaen, height=23, width=44,background='#FEB612')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('textos',foreground='black')
    texto.insert(END,'7.1 Para 2030, garantizar el acceso\n' 
                 'universal a servicios energéticos modernos,\n' 
                 'confiables y asequibles.\n'
                 '7.2 Para 2030 aumentar de significativamente\n' 
                 'la proporción de energías renovables dentro\n' 
                 'del conjunto de fuentes energéticas.\n'
                 '7.3 Para 2030, duplicar la tasa global de\n' 
                 'mejora en la eficiencia energética.\n'
                 '7.a Para 2030, promover la cooperación\n' 
                 'internacional para facilitar el acceso a la\n' 
                 'investigación y tecnología de energía limpia\n' 
                 'como fuentes renovables, eficiencia\n' 
                 'energética y tecnologías avanzadas y menos\n' 
                 'contaminantes de combustibles fósiles, así\n' 
                 'como fomentar la inversión en tecnologías e\n' 
                 'infraestructuras limpias.\n'
                 '7.b Para 2030, expandir la infraestructura y\n' 
                 'mejorar la tecnología para brindar servicios\n' 
                 'energéticos modernos y sostenibles a todos\n' 
                 'en los países en desarrollo, especialmente\n' 
                 'en los países menos adelantados, pequeños\n' 
                 'Estados insulares y países sin acceso al mar\n' 
                 'en línea con sus planes de apoyo.','textos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://wordwall.net/es/resource/39519138/ciencias-naturales/ods-7-energ%c3%ada-asequible-y-no-contaminante')
    
    btnlink=Button(ventanaen,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    saliren=ventanaen.destroy
    btnsaliren=Button(ventanaen,text='Volver',font=('Arial',12,'bold'),foreground='red',command=saliren).place(x=725,y=550)

    a=Image.open('ods7.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanaen,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Trabajo():
    ventanat=Toplevel()
    ventanat.title("Trabajo Desente y Crecimiento Económico")
    ventanat.config(bg="#8F1838")
    ventanat.geometry("830x600")
    ventanat.iconbitmap('pensionado.ico')
    ventanat.resizable(0,0)
    
    lbltitulot=Label(ventanat,text='Trabajo Desente y Crecimiento Económico',background='#8F1838',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanat, height=28, width=52,background='#8F1838')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'Este objetivo busca fomentar un crecimiento\n' 
                 'económico inclusivo y sostenible, junto con la\n' 
                 'creación de empleo y condiciones laborales dignas\n' 
                 'para todos. Sin embargo, múltiples crisis amenazan\n' 
                 'la economía global, y se espera una desaceleración\n' 
                 'en el crecimiento real del PIB per cápita en 2023.\n\n' 
                 'Las dificultades económicas están llevando a más\n' 
                 'personas hacia el empleo informal.\n\n'
                 'A pesar de los avances, como el aumento de la\n' 
                 'productividad laboral y la disminución del desempleo\n'
                 'global, es crucial seguir mejorando las\n' 
                 'oportunidades laborales, especialmente para los\n' 
                 'jóvenes. Además, se debe reducir el empleo informal,\n' 
                 'abordar la desigualdad en el mercado laboral (en\n' 
                 'particular, la brecha salarial entre hombres y\n' 
                 'mujeres), promover ambientes laborales seguros y\n' 
                 'ampliar el acceso a servicios financieros para\n' 
                 'asegurar un crecimiento económico inclusivo y\n' 
                 'sostenido.\n\n'
                 'El cumplimiento de este objetivo tambien nos puede\n'
                 'ayudar a solventar el objetivo 1 pues recordemos\n'
                 'que la ONU nos dice que una de las principales\n'
                 'causas de pobreza es la falta de empleo.','blancodos')
#
    texto.config(state=DISABLED)

    texto=Text(ventanat, height=23, width=44,background='#8F1838')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'8.1 Mantener el crecimiento per cápita de\n' 
                 'acuerdo con las circunstancias nacionales, y\n' 
                 'en los países menos desarrollados, lograr un\n' 
                 'crecimiento del PIB de al menos el 7% anual.\n'
                 '8.2 Alcanzar mayore nivel de productividad\n' 
                 'mediante la diversificación, modernización\n' 
                 'tecnológica y la innovación, con un enfoque\n' 
                 'en sectores de alto valor añadido y uso\n' 
                 'intensivo de mano de obra.\n'
                 '8.3 Promover políticas de desarrollo que\n' 
                 'apoyen la creación de empleos dignos, el\n' 
                 'emprendimiento, la creatividad y la\n' 
                 'innovación y fomentar la formalización y\n'
                 'crecimiento de microempresas y pequeñas y\n' 
                 'medianas empresas, mediante el acceso a\n' 
                 'servicios financieros.\n'
                 '8.4 Mejorar de manera progresiva la\n' 
                 'eficiencia en el uso de recursos y\n' 
                 'desvincular el crecimiento económico de\n' 
                 'la degradación ambiental de aquí a 2030,\n' 
                 'comenzando por los países desarrollados, de\n' 
                 'acuerdo con el Marco Decenal de Programas\n' 
                 'sobre Consumo y Producción Sostenibles.\n'
                 '8.5 Para 2030, lograr el empleo pleno y\n' 
                 'productivo, con trabajo digno para todas las\n' 
                 'personas, incluyendo jóvenes y personas con\n' 
                 'discapacidad, y garantizar la igualdad\n' 
                 'salarial por trabajo de igual valor.\n'
                 '8.6 Reducir considerablemente, antes de 2020\n' 
                 'la proporción de jóvenes que no están\n' 
                 'empleados ni cursan estudios o formación.\n'
                 '8.7 Adoptar medidas para erradicar el\n' 
                 'trabajo forzoso, las formas modernas de\n' 
                 'esclavitud y la trata de personas, y\n' 
                 'eliminar las formas de trabajo infantil,\n' 
                 'incluyendo el uso de niños soldados, con el\n' 
                 'objetivo de erradicar el trabajo infantil en\n' 
                 'todas sus formas antes de 2025.\n'
                 '8.8 Proteger los derechos laborales y\n' 
                 'promover un entorno de trabajo seguro y\n' 
                 'saludable para todos los trabajadores,\n' 
                 'especialmente migrantes, mujeres migrantes\n' 
                 'y personas con empleos precarios.\n'
                 '8.9 Para 2030, implementar políticas que\n' 
                 'fomenten un turismo sostenible, que cree\n' 
                 'empleos y promueva la cultura y productos\n' 
                 'locales.\n'
                 '8.10 Fortalecer las instituciones\n' 
                 'financieras nacionales para aumentar el\n' 
                 'acceso a servicios bancarios, financieros\n' 
                 'y de seguros para todos.\n'
                 '8.a Aumentar el apoyo a la iniciativa de\n' 
                 'ayuda para el comercio en los países en\n' 
                 'desarrollo, especialmente en los menos\n' 
                 'adelantados, mediante el Marco Integrado\n' 
                 'Mejorado para la Asistencia Técnica en\n'
                 'Comercio.\n'
                 '8.b Desarrollar y poner en marcha, antes de\n' 
                 '2030, una estrategia global para el empleo\n' 
                 'juvenil, y aplicar el Pacto Mundial para el\n' 
                 'Empleo de la Organización Internacional del\n'
                 'Trabajo.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://wordwall.net/resource/71372434/ods-8-trabajo-decente-y-crecimiento-economico')
    
    btnlink=Button(ventanat,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)
    
    salirt=ventanat.destroy
    btnsalirt=Button(ventanat,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirt).place(x=725,y=550)

    a=Image.open('ods8.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanat,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Industria():
    ventanain=Toplevel()
    ventanain.title("Industria, Innovación e Infraestructura")
    ventanain.config(bg="#F16E25")
    ventanain.geometry("830x600")
    ventanain.iconbitmap('pensionado.ico')
    ventanain.resizable(0,0)

    lbltituloin=Label(ventanain,text='Industria, Innovación e Infraestructura',background='#F16E25',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanain, height=28, width=52,background='#F16E25')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'Este objetivo busca crear infraestructuras más\n' 
                 'resilientes, promover a industrialización\n' 
                 'sostenible y fomentar la innovación. El crecimiento\n' 
                 'económico, el desarrollo social y las acciones\n' 
                 'contra el cambio climático dependen en gran medida\n' 
                 'de inversiones en infraestructuras, el desarrollo\n' 
                 'industrial sostenible y los avances tecnológicos.\n\n' 
                 'Dado el rápido cambio del panorama económico global\n' 
                 'y el aumento de las desigualdades, es crucial que\n' 
                 'el crecimiento económico esté basado en una\n' 
                 'industrialización inclusiva y en infraestructuras\n' 
                 'resistentes, apoyándose en la innovación.\n\n'
                 'Este objetivo incluye el desarrollo de industrias\n'
                 'inclusivas y sostenibles, promobiendo el transporte,\n'
                 'el uso de energías renovables y las Tecnologías de\n'
                 'la Información y la Comunicación (TIC´s)\n\n'
                 'Para la realización de este objetivo no solo se debe\n'
                 'impulzar las empresas gubernamentales, pues también\n'
                 'es necesario apoyar a la empresa privada de los\n'
                 'países que necesitan recursos tecnológicos y\n' 
                 'financieros','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanain, height=23, width=44,background='#F16E25')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'9.1 Desarrollar infraestructuras confiables,\n' 
                 'sostenibles, resilientes y de calidad,\n' 
                 'incluidas aquellas transfronterizas y\n' 
                 'regionales, para respaldar el desarrollo\n' 
                 'económico y el bienestar humano, asegurando\n' 
                 'un acceso equitativo y asequible para todos.\n'
                 '9.2 Impulsar una industrialización inclusiva\n' 
                 'y sostenible y aumentar significativamente\n' 
                 'la participación de la industria en el\n' 
                 'empleo y el PIB, adaptándose a las distintas\n' 
                 'circunstancias de cada país, y duplicar esta\n' 
                 'participación en los países poco adelantados'
                 '9.3 Mejorar el acceso de pequeñas industrias\n' 
                 'y empresas, especialmente en países en\n' 
                 'desarrollo, a servicios financieros, como\n' 
                 'créditos accesibles, y facilitar su\n' 
                 'integración en las cadenas de valor y los\n' 
                 'mercados.\n'
                 '9.4 Modernizar las infraestructuras y\n' 
                 'transformar las industrias para que sean\n' 
                 'más sostenibles, utilizando los recursos de\n' 
                 'manera eficiente, promoviendo tecnologías\n' 
                 'limpias y respetuosas con el medio ambiente,\n' 
                 'con acciones adaptadas a las capacidades de\n' 
                 'cada país.\n'
                 '9.5 Incrementar la investigación científica\n' 
                 'y mejorar las capacidades tecnológicas de\n' 
                 'los sectores industriales en todos los\n' 
                 'países, especialmente en los países en\n' 
                 'desarrollo, fomentando la innovación y\n' 
                 'aumentando considerablemente para 2030 el\n' 
                 'número de personas dedicadas a la\n' 
                 'investigación y el desarrollo por millón\n' 
                 'de habitantes, así como la inversión en\n' 
                 'I+D en los sectores público y privado.\n'
                 '9.a Facilitar el desarrollo de varias\n' 
                 'infraestructuras sostenibles y\n' 
                 'resilientes en los países en desarrollo,\n' 
                 'ofreciendo mayor apoyo financiero,\n' 
                 'tecnológico y técnico a los países\n' 
                 'africanos, menos desarrollados, sin\n' 
                 'litoral y pequeños Estados insulares.\n'
                 '9.b Apoyar el desarrollo de tecnologías,\n'
                 'la investigación y la innovación en los\n' 
                 'países en desarrollo, asegurando un\n' 
                 'entorno regulatorio favorable para la\n' 
                 'diversificación industrial y la generación\n' 
                 'de valor añadido en productos básicos.\n'
                 '9.c Aumentar significativamente el acceso\n' 
                 'a las tecnologías de la información y las\n' 
                 'comunicaciones, y esforzarse por brindar\n' 
                 'acceso universal y asequible a Internet en\n' 
                 'los países menos desarrollados para 2030.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://wordwall.net/resource/61232142/industria-innovaci%C3%B3n-e-infraestructura')
    
    btnlink=Button(ventanain,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)
    
    salirin=ventanain.destroy
    btnsalirin=Button(ventanain,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirin).place(x=725,y=550)

    a=Image.open('ods9.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanain,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Desigualdad():
    ventanad=Toplevel()
    ventanad.title("Reducción de la Desigualdad")
    ventanad.config(bg="#DE1267")
    ventanad.geometry("830x600")
    ventanad.iconbitmap('pensionado.ico')
    ventanad.resizable(0,0)

    lbltitulod=Label(ventanad,text='Reducción de la Desigualdad',background='#DE1267',font=('Arial',14,'bold')).place(x=100,y=20)

    texto=Text(ventanad, height=28, width=52,background='#DE1267')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'La desigualdad amenaza el desarrollo social y \n'
                 'económico a largo plazo, frena la reducción de la \n'
                 'pobreza y destruye el sentido de realización y \n'
                 'autoestima de las personas.\n\n' 
                 'En la mayoría de los países, los ingresos del 40%\n' 
                 'más pobre de la población aumentaron con mayor \n'
                 'rapidez que la media nacional. Sin embargo, los \n'
                 'últimos datos, aún no concluyentes, sugieren que la\n'
                 'COVID-19 puede haber perjudicado esta tendencia \n'
                 'positiva de reducción de la desigualdad dentro de\n'
                 'los países. Debido a esto, la desigualdad por razón\n'
                 'de ingresos, sexo, edad, discapacidad, orientación\n'
                 'sexual, raza, clase, etnia, religión, así como la\n'
                 'desigualdad de oportunidades, genera amenazas para\n'
                 'el desarrollo social y económico a largo plazo,\n'
                 'frenando la reducción de la pobreza y destruye el\n' 
                 'sentido de realización y autoestima de las personas\n'
                 'resultando en delincuencia, enfermedades y daño\n' 
                 'ambiental.\n\n' 
                 'Difícilmente se logrará un desarrollo sostenible \n'
                 'privando a la gente de una mejor calidad de vida.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanad, height=23, width=44,background='#DE1267')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'10.1 De aquí a 2030, lograr progresivamente\n' 
                 'y mantener el crecimiento de ingresos del\n' 
                 '40% más pobre de la población a una tasa \n'
                 'superior a la media nacional.\n'
                 '10.2 De aquí a 2030, potenciar y promover la\n'
                 'inclusión social, económica y política de\n'
                 'todas las personas, independientemente de su\n'
                 'edad, sexo, discapacidad, raza, etnia,\n' 
                 'origen, religión, situación económica u otra\n'
                 'condición.\n'
                 '10.3 Garantizar la igualdad de oportunidades\n' 
                 'y reducir la desigualdad de resultados,\n' 
                 'incluso eliminando las leyes, políticas y\n' 
                 'prácticas discriminatorias y promoviendo\n'
                 'legislaciones, políticas y medidas adecuadas\n'
                 'a ese respecto.\n'
                 '10.4 Adoptar políticas, salariales y de\n'
                 'protección social, y lograr progresivamente una mayor igualdad.\n'
                 '10.5 Mejorar la reglamentación y vigilancia\n' 
                 'de las instituciones y los mercados\n' 
                 'financieros mundiales y fortalecer la\n'
                 'aplicación de esos reglamentos.\n'
                 '10.6 Asegurar una mayor representación e\n' 
                 'intervención de los países en desarrollo en\n' 
                 'las decisiones acogidas por las distintas\n'
                 'instituciones económicas y financieras \n'
                 'internacionales para aumentar la eficacia,\n'
                 'fiabilidad y veracidad de las instituciones.\n'
                 '10.7 Facilitar la migración y la movilidad\n' 
                 'ordenadas, seguras, regulares y responsables\n'
                 'de las personas, incluso mediante la\n'
                 'aplicación de políticas migratorias bien\n'
                 'planificadas y bien gestionadas.','blancodos')  
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://es.educaplay.com/recursos-educativos/7269241-reduccion_de_las_desigualdades.html')
    
    btnlink=Button(ventanad,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    salird=ventanad.destroy
    btnsalird=Button(ventanad,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salird).place(x=725,y=550)

    a=Image.open('ods10.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanad,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Ciudad():
    ventanac=Toplevel()
    ventanac.title("Ciudades y Comunidades Sostenibles")
    ventanac.config(bg="#F99D25")
    ventanac.geometry("830x600")
    ventanac.iconbitmap('pensionado.ico')
    ventanac.resizable(0,0)

    lbltituloc=Label(ventanac,text='Ciudades y Comunidades Sostenibles',background='#F99D25',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanac, height=28, width=52,background='#F99D25')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'El Objetivo 11 pretende lograr que las ciudades y\n'
                 'los asentamientos humanos sean inclusivos, seguros,\n' 
                 'resilientes y sostenibles.\n\n'
                 'Las ciudades representan el futuro del modo de vida\n'
                 'global. La población mundial alcanzó los 8000\n'
                 'millones de personas en 2022, de las cuales más de\n'
                 'la mitad viven en zonas urbanas. Se prevé que esta\n'
                 'cifra aumente y que para 2050 el 70% de la población\n'
                 'vivirá en ciudades.\n\n'
                 'Aproximadamente 1100 millones de personas viven\n' 
                 'actualmente en barrios marginales, o en condiciones\n' 
                 'similares en las ciudades, y se espera que en 30\n' 
                 'años haya 2000 millones más. Sin embargo, muchas\n' 
                 'de estas ciudades no están preparadas para esta\n'
                 'rápida urbanización, y el desarrollo de la vivienda,\n'
                 'las infraestructuras y los servicios se ve superado,\n' 
                 'lo que provoca un crecimiento de los barrios\n'
                 'marginales o de condiciones similares.\n\n'
                 'El crecimiento caótico urbano, la contaminación\n' 
                 'atmosférica y la escasez de espacios públicos\n' 
                 'persisten en las ciudades.','blancodos') 
    texto.config(state=DISABLED)

    texto=Text(ventanac, height=23, width=44,background='#F99D25')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'11.1 De aquí a 2030, asegurar el acceso de\n' 
                 'todas las personas a viviendas y servicios\n' 
                 'básicos adecuados, seguros y asequibles y\n' 
                 'mejorar los barrios marginales.\n'
                 '11.2 De aquí a 2030, proporcionar acceso a\n' 
                 'sistemas de transporte seguros, asequibles y\n' 
                 'sostenibles para todos mejorando la\n' 
                 'seguridad vial, en particular mediante la\n' 
                 'ampliación del transporte público, prestando\n'
                 'especial atención a las necesidades de las\n' 
                 'personas en situación de vulnerabilidad, las\n' 
                 'mujeres, los niños, las personas que poseen\n'
                 'una discapacidad y las personas de edad.\n'
                 '11.3 Hasta 2030, aumentar la urbanización\n' 
                 'inclusiva y sostenible, la capacidad para la\n' 
                 'planificación y la gestión participativas,\n' 
                 'integradas y sostenibles de asentamientos\n' 
                 'humanos en todos los países.\n'
                 '11.4 Redoblar los esfuerzos para proteger y\n' 
                 'salvaguardar el patrimonio cultural y\n' 
                 'natural del mundo.\n'
                 '11.5 De aquí a 2030, poder reducir\n' 
                 'significativamente el número de muertes\n' 
                 'causadas por los desastres, incluidos los\n' 
                 'relacionados con el agua, y de personas\n' 
                 'afectadas por ellos, y de este modo reducir\n' 
                 'considerablemente las pérdidas económicas\n' 
                 'directas provocadas por los desastres en\n' 
                 'comparación con el PIB mundial.\n'
                 '11.6 De aquí a 2030, reducir el impacto\n' 
                 'ambiental negativo per cápita de las\n' 
                 'ciudades, incluso prestando especial\n' 
                 'atención a la calidad del aire y la gestión\n' 
                 'de los desechos municipales y de otro tipo.\n'
                 '11.7 De aquí a 2030, proporcionar acceso\n' 
                 'universal a zonas verdes y espacios públicos\n' 
                 'seguros, inclusivos y accesibles, en\n' 
                 'particular para las mujeres y los niños, las\n' 
                 'personas de edad y las discapacitadas.','blancodos')
    texto.config(state=DISABLED)
    
    def linkp ():
        webbrowser.open('https://es.educaplay.com/recursos-educativos/7907203-ciudades_y_comunidades.html')
    
    btnlink=Button(ventanac,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    salirc=ventanac.destroy
    btnsalirc=Button(ventanac,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirc).place(x=725,y=550)

    a=Image.open('ods11.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanac,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Producción():
    ventanapr=Toplevel()
    ventanapr.title("Producción y Consumo Responsables")
    ventanapr.config(bg="#CD8C2E")
    ventanapr.geometry("830x600")
    ventanapr.iconbitmap('pensionado.ico')
    ventanapr.resizable(0,0)

    lbltitulopr=Label(ventanapr,text='Producción y Consumo Responsables',background='#CD8C2E',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanapr, height=28, width=52,background='#CD8C2E')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'El Objetivo 12 pretende garantizar modalidades de\n' 
                 'consumo y producción sostenibles, algo fundamental\n' 
                 'para sostener los medios desubsistencia de las\n' 
                 'generaciones actuales y futuras.\n\n'
                 'Nuestro planeta se está quedando sin recursos,\n' 
                 'pero el índice de población sigue creciendo. En\n' 
                 'caso de que la población mundial alcance los 9800\n' 
                 'millones de personas en 2050, se podría necesitar el\n' 
                 'equivalente a casi tres planetas para proporcionar\n' 
                 'los recursos naturales necesarios para mantener los\n' 
                 'estilos de vida actuales.\n\n'
                 'Para reducir nuestros niveles de consumo, debemos\n' 
                 'cambiar nuestros hábitos, y una de las principales\n' 
                 'medidas que debemos adoptar es sustituir los \n' 
                 'sistemas de suministro energético por otros más\n'
                 'sostenibles.\n\n'
                 'Abordar la pérdida de alimentos es urgente y \n' 
                 'requiere políticas basadas en datos, así como\n' 
                 'inversiones en tecnologías, infraestructuras,\n' 
                 'enseñanza y supervisión. A pesar de que una gran\n' 
                 'parte de la población mundial pasa hambre, cada año\n' 
                 'se desperdicia la asombrosa cantidad de 931 millones\n' 
                 'de toneladas de alimentos.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanapr, height=23, width=44,background='#CD8C2E')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'12.1 Aplicar el Marco Decenal de Programas\n' 
                 'sobre Modalidades de Consumo y Producción\n' 
                 'Sostenibles, con la participación de todos\n' 
                 'los países y bajo el liderazgo de los países\n' 
                 'desarrollados, teniendo en cuenta el grado\n' 
                 'de desarrollo y las capacidades de los\n' 
                 'países en desarrollo.\n'
                 '12.2 De aquí a 2030, lograr la gestión\n' 
                 'sostenible y el uso idóneo de los recursos\n' 
                 'naturales.\n'
                 '12.3 De aquí a 2030, reducir a la mitad el\n' 
                 'desperdicio de alimentos per cápita mundial\n' 
                 'en la venta al por menor y a nivel de los\n' 
                 'consumidores y reducir las pérdidas de\n' 
                 'alimentos en las cadenas de producción y\n' 
                 'suministro, incluidas las pérdidas\n' 
                 'posteriores a la cosecha.\n'
                 '12.5 Hasta 2030, reducir considerablemente\n' 
                 'la generación de desechos mediante\n' 
                 'actividades de prevención, reducción,\n' 
                 'reciclado y reutilización\n'
                 '12.6 Alentar a las empresas, en especial las\n' 
                 'grandes empresas y las transnacionales,\n' 
                 'a que adopten prácticas sostenibles e\n' 
                 'incorporen información sobre la factibilidad\n' 
                 'en su ciclo de presentación de informes.\n'
                 '12.7 Promover prácticas de adquisición\n' 
                 'pública que sean sostenibles, de conformidad\n' 
                 'con las políticas y prioridades nacionales.\n'
                 '12.8 Hasta 2030, asegurar que las personas\n' 
                 'de todo el mundo tengan la información y\n' 
                 'los conocimientos pertinentes para el\n' 
                 'desarrollo sostenible y los estilos de vida\n' 
                 'en armonía con la naturaleza.','blancodos') 
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://es.educaplay.com/recursos-educativos/13407066-objetivo_12_produccion_y_consumo.html')
    
    btnlink=Button(ventanapr,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)
    
    salirpr=ventanapr.destroy
    btnsalirpr=Button(ventanapr,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirpr).place(x=725,y=550)

    a=Image.open('ods12.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanapr,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Clima():
    ventanacl=Toplevel()
    ventanacl.title("Acción por el Clima")
    ventanacl.config(bg="#217045")
    ventanacl.geometry("830x600")
    ventanacl.iconbitmap('pensionado.ico')
    ventanacl.resizable(0,0)

    lbltitulocl=Label(ventanacl,text='Acción por el Clima',background='#217045',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanacl, height=28, width=52,background='#217045')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'El cambio climático se debe a las actividades\n' 
                 'humanas y amenaza la vida en la Tierra tal como la\n' 
                 'conocemos. Con el aumento de las emisiones de gases\n' 
                 'de efecto invernadero, el cambio climático\n' 
                 'evoluciona a un ritmo mucho más rápido de lo\n' 
                 'previsto. Sus efectos pueden ser devastadores y\n' 
                 'pueden provocar fenómenos meteorológicos extremos y\n' 
                 'cambiantes, así como la subida del nivel del mar.\n\n'
                 'De no controlarse, el cambio climático echará por\n' 
                 'tierra muchos de los avances logrados en materia de\n' 
                 'desarrollo en los últimos años.\n\n'
                 'Es crucial tomar medidas urgentes y transformadoras\n' 
                 'que vayan más allá de meras promesas. Esto exige\n' 
                 'aumentar las ambiciones, abarcar economías enteras\n' 
                 'y avanzar hacia un desarrollo resiliente al clima,\n' 
                 'al tiempo que se traza una trayectoria clara para\n' 
                 'lograr cero emisiones netas. El tiempo se acaba y\n' 
                 'es necesario tomar medidas inmediatas para evitar\n' 
                 'consecuencias catastróficas y garantizar un futuro\n' 
                 'sostenible a las generaciones venideras\n'
                 'Se puede decir que esta ODS se a combertido en un\n' 
                 'objetivo principal ya que segun el NASA Eart\n' 
                 'Observatory (2023) se registró que el año 2023 a\n' 
                 'sido el año con las temperaturas más altas de la\n' 
                 'historia se registró que el verano de 2023 tubo\n' 
                 '1.17°C extra de la temperatura abitual y los\n' 
                 'estudios nos dicen que ese aumento se da debido a\n' 
                 'la emición de gases de efecto invernadero por\n' 
                 'parte del ser humano.','blancodos') 
    texto.config(state=DISABLED)

    texto=Text(ventanacl, height=23, width=44,background='#217045')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'13.1 Fortalecer la resiliencia y capacidad\n' 
                 'de adaptación a los riesgos relacionados con\n' 
                 'el clima y los desastres naturales en todos\n' 
                 'los países.\n'
                 '13.2 Incorporar medidas relativas al cambio\n' 
                 'climático en las políticas, estrategias y\n' 
                 'planes nacionales.'
                 '13.3 Mejorar la educación, sensibilización\n' 
                 'y capacidad humana e institucional respecto\n' 
                 'de la mitigación del cambio climático, la\n' 
                 'adaptación a él, la reducción de sus efectos\n' 
                 'y la alerta temprana.\n'
                 '13.a Cumplir el compromiso de los países\n' 
                 'desarrollados que son parte en la Convención\n' 
                 'Marco de las Naciones Unidas sobre el Cambio\n'
                 'Climático de lograr para el año 2020 el\n' 
                 'objetivo de movilizarconjuntamente 100.000\n' 
                 'millones de dólares anuales procedentes de\n' 
                 'todas las fuentes a fin de atender las\n' 
                 'necesidades de los países en desarrollo\n' 
                 'respecto de la adopción de medidas concretas\n' 
                 'de mitigación y la transparencia de su\n' 
                 'aplicación, y poner en pleno funcionamiento\n' 
                 'el Fondo Verde para el Clima capitalizándolo\n' 
                 'lo antes posible.\n'
                 '13.b Promover mecanismos para aumentar la\n' 
                 'capacidad para la planificación y gestión\n' 
                 'eficaces en relación con el cambio climático\n' 
                 'en los países menos adelantados y los\n' 
                 'pequeños Estados insulares en desarrollo,\n' 
                 'haciendo particular hincapié en las mujeres,\n' 
                 'los jóvenes y las comunidades locales y\n' 
                 'marginadas','blancodos') 
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://es.educaplay.com/recursos-educativos/19237841-ods_13_accion_por_el_clima.html')
    
    btnlink=Button(ventanacl,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)
    
    salircl=ventanacl.destroy
    btnsalircl=Button(ventanacl,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salircl).place(x=725,y=550)

    a=Image.open('ods13.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanacl,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Submarino():
    ventanasb=Toplevel()
    ventanasb.title("Vida Submarina")
    ventanasb.config(bg="#007CBB")
    ventanasb.geometry("830x600")
    ventanasb.iconbitmap('pensionado.ico')
    ventanasb.resizable(0,0)

    lbltitulosb=Label(ventanasb,text='Vida Submarina',background='#007CBB',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanasb, height=28, width=52,background='#007CBB')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'Este objetivo pretende conservar y utilizar\n' 
                 'sosteniblemente los océanos, mares y los recursos\n' 
                 'marinos. La existencia humana y la vida en la Tierra\n' 
                 'dependen de unos océanos y mares sanos.\n\n'
                 'Los océanos son intrínsecos a nuestra vida en la\n' 
                 'Tierra. Cubren tres cuartas partes de la superficie\n' 
                 'terrestre, contienen el 97% del agua de la Tierra y\n' 
                 'representan el 99% del espacio vital del planeta por\n' 
                 'volumen.\n\n'
                 'Proporcionan recursos clave como alimento, medicina,\n' 
                 'biocombustible y otros productos; nos ayudan a\n' 
                 'descomponer y eliminar los residuos y a reducir la\n' 
                 'contaminación; y las variadas costas contribuyen\n' 
                 'a reducir los daños causados por las tormentas.\n\n'
                 'La contaminación marina está alcanzando niveles\n' 
                 'extremos. Más de 17 millones de toneladas métricas\n' 
                 'contaminaban el océano en 2021, cifra que se\n' 
                 'duplicará o triplicará para el año 2040, lo que\n' 
                 'resulta preocupante. La gestión responsable de este\n' 
                 'vital recurso mundial es una de las claves de un\n' 
                 'futuro sostenible.','blancodos') 
    texto.config(state=DISABLED)

    texto=Text(ventanasb, height=23, width=44,background='#007CBB')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'14.1 De aquí a 2025, prevenir y reducir\n' 
                 'significativamente la contaminación marina\n' 
                 'de todo tipo, en particular la producida por\n'
                 'actividades realizadas en tierra, incluidos\n' 
                 'los detritos marinos y la polución por\n' 
                 'nutrientes.\n'
                 '14.3 Minimizar y abordar los efectos de la\n' 
                 'acidificación de los océanos, mediante una\n' 
                 'mayor cooperación científica a todos los\n' 
                 'niveles.\n'
                 '14.7 De aquí a 2030, aumentar los beneficios\n' 
                 'económicos que los pequeños Estados\n' 
                 'insulares en desarrollo y los países menos\n' 
                 'adelantados obtienen del uso sostenible de\n' 
                 'los recursos marinos, en particular mediante\n' 
                 'la gestión sostenible de la pesca, la\n' 
                 'acuicultura y el turismo.\n'
                 '14.a Aumentar los conocimientos científicos,\n' 
                 'desarrollar la capacidad de investigación y\n' 
                 'transferir tecnología marina, teniendo en\n' 
                 'cuenta los Criterios y Directrices para la\n' 
                 'Transferencia de Tecnología Marina de la\n' 
                 'Comisión Oceanográfica Intergubernamental,\n' 
                 'a fin de mejorar la salud de los océanos y\n' 
                 'potenciar la contribución de la\n' 
                 'biodiversidad marina al desarrollo de los\n' 
                 'países en desarrollo, en particular los\n' 
                 'pequeños Estados insulares en desarrollo y\n' 
                 'los países menos adelantados.\n'
                 '14.b Facilitar el acceso de los pescadores\n' 
                 'artesanales a los recursos marinos y los\n' 
                 'mercados.','blancodos') 
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://view.genially.com/66f4c733d2a395bf2d6ae079/interactive-content-escape-viaje-submarino')
    
    btnlink=Button(ventanasb,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)
    
    salirsb=ventanasb.destroy
    btnsalirsb=Button(ventanasb,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirsb).place(x=725,y=550)

    a=Image.open('ods14.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanasb,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Terrestre():
    ventanatr=Toplevel()
    ventanatr.title("Vida de Ecosistemas Terrestres")
    ventanatr.config(bg="#3EB049")
    ventanatr.geometry("830x600")
    ventanatr.iconbitmap('pensionado.ico')
    ventanatr.resizable(0,0)

    lbltitulotr=Label(ventanatr,text='Vida de Ecosistemas Terrestres',background='#3EB049',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanatr, height=28, width=52,background='#3EB049')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'El Objetivo 15 pretende conservar la vida de los\n' 
                 'ecosistemas terrestres. Busca proteger y restablecer\n' 
                 'los ecosistemas terrestres, gestionar de forma\n' 
                 'sostenible los bosques, luchar a toda costa contra\n' 
                 'la desertificación, invertir la degradación de las\n' 
                 'tierras, y detener la pérdida de biodiversidad.\n\n'
                 'Los ecosistemas terrestres son vitales para el\n' 
                 'sostenimiento de la vida humana, contribuyen a\n' 
                 'más de la mitad del PIB mundial e incluyen\n' 
                 'diversos valores culturales, espirituales y\n' 
                 'económicos.\n\n'
                 'Sin embargo, el mundo se enfrenta a una triple\n' 
                 'crisis del cambio climático, a la contaminación\n' 
                 'y a la pérdida de la biodiversidad. Más de 100\n' 
                 'millones de hectáreas de tierras sanas y\n' 
                 'productivas se degradaron anualmente entre 2015\n' 
                 'y 2019, lo que afectó a la vida de 1300 millones\n' 
                 'de personas. Para cumplir el Objetivo 15, es\n' 
                 'esencial un cambio fundamental en la relación de\n' 
                 'la humanidad con la naturaleza, y tomar\n' 
                 'conciencia de que la naturaleza es la base de\n' 
                 'nuestra vida en la Tierra.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanatr, height=23, width=44,background='#3EB049')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'15.3 Luchar contra la desertificación,\n' 
                 'rehabilitar las tierras y suelos degradados,\n' 
                 'incluidas las tierras afectadas por la\n' 
                 'desertificación, sequía y las inundaciones,\n' 
                 'y procurar lograr un mundo con una\n' 
                 'degradación neutra del suelo.\n'
                 '15.4 Para 2030, velar por la conservación\n' 
                 'de los ecosistemas montañosos, incluida su\n' 
                 'diversidad biológica, a fin de mejorar su\n' 
                 'capacidad de proporcionar beneficios\n' 
                 'esenciales para el desarrollo sostenible.\n'
                 '15.5 Adoptar medidas significativas y\n' 
                 'urgentes para reducir la degradación de\n' 
                 'los hábitats naturales, detener la pérdida\n' 
                 'de la diversidad biológica.\n'
                 '15.6 Promover la participación justa y\n' 
                 'equitativa en los beneficios que se deriven\n' 
                 'de la utilización de los recursos genéticos\n' 
                 'y promover el acceso adecuado a esos\n' 
                 'recursos, como se ha acordado\n' 
                 'internacionalmente.\n'
                 '15.7 Adoptar medidas urgentes para poner fin\n' 
                 'a la caza furtiva y el tráfico de especies\n' 
                 'protegidas de flora y fauna y abordar la\n' 
                 'demanda y la oferta ilegales de productos\n' 
                 'silvestres.\n'
                 '15.a Movilizar y aumentar de manera\n' 
                 'significativa los recursos financieros\n' 
                 'procedentes de todas las fuentes para\n' 
                 'conservar y utilizar de forma sostenible la\n' 
                 'diversidad biológica y los ecosistemas.\n'
                 '15.b Movilizar un volumen apreciable de\n' 
                 'recursos procedentes de todas las fuentes y\n' 
                 'a todos los niveles para financiar la\n' 
                 'gestión forestal sostenible y proporcionar\n' 
                 'incentivos adecuados a los países en\n' 
                 'desarrollo para que promuevan dicha gestión.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://wordwall.net/es/resource/10083411/vida-de-ecosistemas-terrestres')
    
    btnlink=Button(ventanatr,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)
    
    salirtr=ventanatr.destroy
    btnsalirtr=Button(ventanatr,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirtr).place(x=725,y=550)

    a=Image.open('ods15.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanatr,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Paz():
    ventanapz=Toplevel()
    ventanapz.title("Paz, Justicia e Instituciones Sólidas")
    ventanapz.config(bg="#025388")
    ventanapz.geometry("830x600")
    ventanapz.iconbitmap('pensionado.ico')
    ventanapz.resizable(0,0)

    lbltitulopz=Label(ventanapz,text='Paz, Justicia e Instituciones Sólidas',background='#025388',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanapz, height=28, width=52,background='#025388')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'Este objetivo busca crear sociedades pacíficas e\n' 
                 'inclusivas donde se respeten los derechos humanos y\n' 
                 'tratando de priorizar la estabilidad mediante un\n' 
                 'gobierno basado en el Estado de derecho.\n\n'
                 'Este objetivo vio la luz debido al aumento de\n' 
                 'conflictos entre las naciones y personas civiles,\n' 
                 'conflictos armados crecientes y disconformidades\n'
                 'con las ideologías de los pares que generaban cada\n' 
                 'vez más conflictos, no solo en el campo de batalla\n' 
                 'sino que, en la era actual, tambien en el internet.\n\n'
                 'En países como Ecuador se busca lograr este\n' 
                 'objetivo con la concientización a la ciudadania\n' 
                 'con clases de resolución de conflictos y\n' 
                 'buscrando transparentizar sus instituciones\n' 
                 'para generar confianza entre los ciudadanos y\n' 
                 'asi fomentar la paz nacional.\n\n'
                 'Esta ODS es fundamental para la correcta convivencia\n' 
                 'en la sociedad y para poder cumplirla es fundamental\n' 
                 'el respeto de los derechos humanos.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanapz, height=23, width=44,background='#025388')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'16.1 Reducir significativamente todas las\n' 
                 'formas de violencia y las correspondientes\n' 
                 'tasas de mortalidad en todo el mundo.\n'
                 '16.2 Poner fin al maltrato, la explotación,\n' 
                 'la trata y todas las formas de violencia y\n' 
                 'tortura contra los niños.\n'
                 '16.3 Promover el estado de derecho en los\n' 
                 'planos nacional e internacional y garantizar\n' 
                 'la igualdad de acceso a la justicia para\n' 
                 'todos.\n'
                 '16.4 Hasta 2030, reducir significativamente\n' 
                 'las corrientes financieras y de armas\n' 
                 'ilícitas, fortalecer la recuperación y\n' 
                 'devolución de los activos robados y luchar\n' 
                 'contra todas las formas de delincuencia\n' 
                 'organizada.\n'
                 '16.5 Reducir considerablemente la corrupción\n' 
                 'y el soborno en todas sus formas.\n'
                 '16.6 Crear a todos los niveles instituciones\n' 
                 'eficaces y transparentes que rindan cuentas.\n'
                 '16.7 Garantizar la adopción en todos los\n' 
                 'niveles de decisiones inclusivas,\n' 
                 'participativas y representativas que\n' 
                 'respondan a las necesidades.\n'
                 '16.8 Ampliar y fortalecer la participación\n' 
                 'de los países en desarrollo en las\n' 
                 'instituciones de gobernanza mundial.\n'
                 '16.9 De aquí a 2030, proporcionar acceso a\n' 
                 'una identidad jurídica para todos, en\n' 
                 'particular mediante el registro de\n' 
                 'nacimientos.\n'
                 '16.10 Garantizar el acceso público a la\n' 
                 'información y proteger las libertades\n' 
                 'fundamentales, de conformidad con las\n' 
                 'leyes nacionales y los acuerdos\n' 
                 'internacionales.\n'
                 '16.a Fortalecer las instituciones\n' 
                 'nacionales pertinentes, incluso mediante\n' 
                 'la cooperación internacional.\n'
                 '16.b Promover y aplicar leyes y políticas\n' 
                 'no discriminatorias en favor del\n' 
                 'desarrollo sostenible.','blancodos')
    texto.config(state=DISABLED)

    def linkp ():
        webbrowser.open('https://view.genially.com/660da55cf5019200154fe1ce/interactive-content-16-paz-justicia-e-instituciones-solidas-juegoparque-de-diversiones')
    
    btnlink=Button(ventanapz,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)
    
    salirpz=ventanapz.destroy
    btnsalirpz=Button(ventanapz,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirpz).place(x=725,y=550)

    a=Image.open('ods16.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanapz,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def Alianza():
    ventanaal=Toplevel()
    ventanaal.title("Alianzas para lograr los Objetivos")
    ventanaal.config(bg="#183668")
    ventanaal.geometry("830x600")
    ventanaal.iconbitmap('pensionado.ico')
    ventanaal.resizable(0,0)

    lbltituloal=Label(ventanaal,text='Alianzas para lograr los Objetivos',background='#183668',font=('Arial',14,'bold')).place(x=100,y=20)
    
    texto=Text(ventanaal, height=28, width=52,background='#183668')
    texto.place(x=30, y=75)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Concepto:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'Esta ODS busca la cooperación de Norte-Sur para\n' 
                 'poder cumplir los planes de todas las naciones del\n' 
                 'mundo fomentando asi valores como la fraternidad.\n\n'
                 'Actualmente esta ODS se destaca por buscar lograr\n' 
                 'completar el acuerdo de Montreal el cual se basa en\n' 
                 'trabajar juntos para proteger la capa de ozono,\n' 
                 'pues es responsabilidad de todas las naciones el\n' 
                 'proteger el planeta y basandonos en esto, gracias\n' 
                 'a la colaboración de todas las naciones se cumple\n' 
                 'la meta 17.3 (Movilizar recursos financieros\n' 
                 'adicionales para los países en desarrollo de\n' 
                 'múltiples fuentes), pero como se cumple esa meta,\n' 
                 'la respuesta es muy sensilla los países en vías\n' 
                 'de desarrollo no pueden destinar suficientes\n' 
                 'recursos a la resolución del acuerdo de Montral\n' 
                 'aqui entran las alianzas pues los países más\n' 
                 'desarrollados pueden ayudar a esas naciones con\n' 
                 'planes de inversión para poder ayudar a lograr el\n' 
                 'objetivo de Montreal e incluso ayudar a que el\n' 
                 'país progrese.\n\n'
                 'En resumen, esta ODS se basa en la cooperación de\n' 
                 'todas las naciones para ofrecer el mejor estilo\n' 
                 'de vida a sus ciudadanos y una economía y\n' 
                 'sociedad estables.','blancodos')
    texto.config(state=DISABLED)

    texto=Text(ventanaal, height=23, width=44,background='#183668')
    texto.place(x=460, y=155)
    texto.tag_configure('blanco',foreground='White',font='bold')
    texto.insert(END,'Metas:\n\n','blanco')
    texto.tag_configure('blancodos',foreground='white')
    texto.insert(END,'17.1 Se debe fortalecer la movilización de\n' 
                 'recursos con el fin de poder mejorar la\n' 
                 'recaudación de ingresos.\n'
                 '17.2 Los países desarrollados deben destinar\n' 
                 'el 0,7% de su ingreso nacional bruto a la\n' 
                 'asistencia oficial para el desarrollo y\n' 
                 'entre el 0,15% y el 0,20% a los países menos\n' 
                 'adelantados.\n'
                 '17.3 Se deben dar recursos financieros a los\n' 
                 'paises en desarrollo desde múltiples fuentes\n'
                 '17.4 Ayudar a los países en desarrollo a\n' 
                 'lograr una sostenibilidad de sus deudas a\n' 
                 'largo plazo.\n'
                 '17.5 Impulsar las inversiones en los paises\n' 
                 'menos desarrollados.\n'
                 '17.6 Mejorar la cooperación regional e\n' 
                 'internacional Norte-Sur y Sur-Sur para\n' 
                 'impulsar el desarrollo científico y\n' 
                 'tecnológico, además de intercambiar en\n' 
                 'conocimiento entre naciones.\n'
                 '17.7 Promover el desarrollo de tecnologías\n' 
                 'ecologicamente racionales y su distrubución\n' 
                 'a el resto de países.\n'
                 '17.9 Incrementar el apoyo internacional\n' 
                 'para fortalecer las capacidades en los\n' 
                 'países en desarrollo, respaldando sus\n' 
                 'planes nacionales para implementar los\n' 
                 'Objetivos de Desarrollo Sostenible mediante\n' 
                 'la cooperación Norte-Sur, Sur-Sur y\n'
                 'triangular.\n'
                 '17.10 Promover el comercio multilateral\n' 
                 'universal.\n'
                 '17.11 Aumentar las exportaciones de los\n' 
                 'países en vias de desarrollo.\n'
                 '17.12 Lograr el acceso libre al mercado de\n' 
                 'forma duradera para los países en vías de\n' 
                 'desarrollo.\n'
                 '17.13 Lograr aumentar la estabilidad\n' 
                 'macroeconómica mundial\n'
                 '17.14 Mejorar las políticas nacionales\n' 
                 'sobre desarrollo sostenible.\n'
                 '17.15 Respetar el liderazgo de cada país\n' 
                 'para estableces políticas que luchen contra\n' 
                 'la pobreza.\n'
                 '17.16 Merorar las alianzas para el\n'
                 'Desarrollo Sostenible y asi movilizar\n' 
                 'conocimiento y tecnologías.\n'
                 '17.17 Fomentar alianzas públias-públicas\n' 
                 'públicas-privadas y en la sociedad civil.\n'
                 '17.19 Aprovechar iniciativas ya existentes\n'
                 'para medir los progresos en desarrollo\n'
                 'sostenible y Producto Interno Bruto.','blancodos')
    texto.config(state=DISABLED)
    
    def linkp ():
        webbrowser.open('https://view.genially.com/66fefc1cf2554cc75ea5fd12/interactive-content-ods-17')
    
    btnlink=Button(ventanaal,text="Jugar",font=('Arial',14,'bold'),command=linkp).place(x=25,y=550)

    saliral=ventanaal.destroy
    btnsaliral=Button(ventanaal,text='Volver',font=('Arial',12,'bold'),foreground='red',command=saliral).place(x=725,y=550)

    a=Image.open('ods17.png')
    a=a.resize((160,130))
    a=ImageTk.PhotoImage(a) 
    lblholah=Label(ventanaal,image=a,border=0).place(x=580,y=20)
    lblholah.pack()
    lblholah.image=a

def fuente():
    ventanaf=Toplevel()
    ventanaf.title("Fuentes")
    ventanaf.config(bg="white")
    ventanaf.geometry("830x375")
    ventanaf.iconbitmap('pensionado.ico')
    ventanaf.resizable(0,0)
    
    lbltitulof=Label(ventanaf,text='Fuentes:',background='White',font=('Arial',14,'bold')).place(x=100,y=20)

    texto=Text(ventanaf, height=15, width=96,background='White')
    texto.place(x=21, y=50)

    texto.tag_configure('negrodos',foreground='black')
    texto.insert(END,'\n\n''1.-NASA Earth Observatory. (2023). Summer 2023 was the hottest on record. Recuperado de https://earthobservatory.nasa.gov/images/151831/summer-2023-was-the-hottest-on-record\n\n' 
                 '2.-ODS Costa Rica. (n.d.). Objetivos de Desarrollo Sostenible. Recuperado de https://ods.cr/\n\n'
                 '3.-ODS Costa Rica. (n.d.). Objetivo 1: Fin de la pobreza. Recuperado de https://ods.cr/es/objetivo/objetivo-1\n\n'
                 '4.-ODS Ecuador. (n.d.). Objetivo 1: Fin de la pobreza. Recuperado de https://www.odsecuador.ec/?p=252\n\n'
                 '5.-United Nations Environment Programme. (n.d.). SDG 17: Partnerships for the Goals. Recuperado de https://ozone.unep.org/sdg17\n\n','negrodos')
    texto.config(state=DISABLED)

    salirf=ventanaf.destroy
    btnsalirf=Button(ventanaf,text='Volver',font=('Arial',12,'bold'),foreground='red',command=salirf).place(x=725,y=320)

##############################################

ventana=Tk()
ventana.title("ODS")
ventana.config(bg="White")
ventana.geometry("830x600")
ventana.iconbitmap('pensionado.ico')
ventana.resizable(0,0)

lbltitulo=Label(ventana,text='Objetivos de Desarrollo Sostenible',background='White',font=('Arial',14,'bold')).place(x=235,y=20)

imgpobreza=Image.open('Finpobreza.png')
imgpobreza=imgpobreza.resize((77,77))
imgpobreza=ImageTk.PhotoImage(imgpobreza)
btnpobreza=Button(ventana,image=imgpobreza,command=Pobreza).place(x=30,y=120)

imghambre=Image.open('Finhambre.png')
imghambre=imghambre.resize((77,77))
imghambre=ImageTk.PhotoImage(imghambre)
btnhambre=Button(ventana,image=imghambre,command=Hambre).place(x=167,y=120)

imgsalud=Image.open('saludbienestar.png')
imgsalud=imgsalud.resize((77,77))
imgsalud=ImageTk.PhotoImage(imgsalud)
btnsalud=Button(ventana,image=imgsalud,command=Salud).place(x=304,y=120)

imgeducacion=Image.open('educacion.png')
imgeducacion=imgeducacion.resize((77,77))
imgeducacion=ImageTk.PhotoImage(imgeducacion)
btneducacion=Button(ventana,image=imgeducacion,command=Educacion).place(x=441,y=120)

imgigualdad=Image.open('igualdad.png')
imgigualdad=imgigualdad.resize((77,77))
imgigualdad=ImageTk.PhotoImage(imgigualdad)
btnigualdad=Button(ventana,image=imgigualdad,command=Igualdad).place(x=578,y=120)

imgagua=Image.open('agua.png')
imgagua=imgagua.resize((77,77))
imgagua=ImageTk.PhotoImage(imgagua)
btnagua=Button(ventana,image=imgagua,command=Agua).place(x=693,y=120)

imgenergia=Image.open('energia.png')
imgenergia=imgenergia.resize((77,77))
imgenergia=ImageTk.PhotoImage(imgenergia)
btnenergia=Button(ventana,image=imgenergia,command=Energia).place(x=30,y=237)

imgtrabajo=Image.open('trabajo.png')
imgtrabajo=imgtrabajo.resize((77,77))
imgtrabajo=ImageTk.PhotoImage(imgtrabajo)
btntrabajo=Button(ventana,image=imgtrabajo,command=Trabajo).place(x=167,y=237)

imgindustria=Image.open('industria.png')
imgindustria=imgindustria.resize((77,77))
imgindustria=ImageTk.PhotoImage(imgindustria)
btnindustria=Button(ventana,image=imgindustria,command=Industria).place(x=304,y=237)

imgdesigualdad=Image.open('desigualdad.png')
imgdesigualdad=imgdesigualdad.resize((77,77))
imgdesigualdad=ImageTk.PhotoImage(imgdesigualdad)
btndesigualdad=Button(ventana,image=imgdesigualdad,command=Desigualdad).place(x=441,y=237)

imgciudad=Image.open('ciudad.png')
imgciudad=imgciudad.resize((77,77))
imgciudad=ImageTk.PhotoImage(imgciudad)
btnciudad=Button(ventana,image=imgciudad,command=Ciudad).place(x=578,y=237)

imgconsumo=Image.open('Consumo.png')
imgconsumo=imgconsumo.resize((77,77))
imgconsumo=ImageTk.PhotoImage(imgconsumo)
btnconsumo=Button(ventana,image=imgconsumo,command=Producción).place(x=693,y=237)

imgclima=Image.open('clima.png')
imgclima=imgclima.resize((77,77))
imgclima=ImageTk.PhotoImage(imgclima)
btnclima=Button(ventana,image=imgclima,command=Clima).place(x=167,y=354)

imgsubmarino=Image.open('submarino.png')
imgsubmarino=imgsubmarino.resize((77,77))
imgsubmarino=ImageTk.PhotoImage(imgsubmarino)
btnsubmarino=Button(ventana,image=imgsubmarino,command=Submarino).place(x=304,y=354)

imgecosistemas=Image.open('ecosistemas.png')
imgecosistemas=imgecosistemas.resize((77,77))
imgecosistemas=ImageTk.PhotoImage(imgecosistemas)
btnecosistemas=Button(ventana,image=imgecosistemas,command=Terrestre).place(x=441,y=354)

imgpaz=Image.open('paz.png')
imgpaz=imgpaz.resize((77,77))
imgpaz=ImageTk.PhotoImage(imgpaz)
btnpaz=Button(ventana,image=imgpaz,command=Paz).place(x=578,y=354)

imgalianza=Image.open('alianza.png')
imgalianza=imgalianza.resize((77,77))
imgalianza=ImageTk.PhotoImage(imgalianza)
btnalianza=Button(ventana,image=imgalianza,command=Alianza).place(x=373,y=471)

btnIA=Button(ventana,text="IA",font=('Arial',14,'bold'),command=linkIA).place(x=25,y=550)

btnF=Button(ventana,text="Fuentes",font=('Arial',14,'bold'),command=fuente).place(x=25,y=20)

salir=ventana.destroy
btnsalir=Button(ventana,text='Salir',font=('Arial',14,'bold'),foreground='red',command=salir).place(x=725,y=550)

ventana.mainloop()
import tkinter as tk
import requests
import config
HEIGHT = 500
WIDTH = 600

root = tk.Tk()

api_key = '4a0875d438bb3d3cacb426086ccc1800'

Canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#5aa8ad')
Canvas.pack()

background_image = tk.PhotoImage(file='C:\\Users\\bhavya\\Documents\\Python Revision\\weather app\\landscape.png')
background = tk.Label(root, image=background_image)
background.place(relheight=1, relwidth=1)


def formatweather(weather):
    try:
        city = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = f'City: {city}\nConditions: {description}\nTemperature (Celcius): {temp}'
    except:
        final_str = 'There was a problem retreiving\ninformation.'

    return final_str


def getweather(city):
    weather_key = config.api_key
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    data = response.json()

    output['text'] = formatweather(data)


def display(entry):
    print("This is a cool function", entry)


Frame = tk.Frame(root, bg='#9dc0d1', bd=5)
Frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(Frame, bg='white', font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(Frame, text='Get Weather', font=('Courier', 10),
                   command=lambda: getweather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#9dc0d1', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6,
                  relwidth=0.75, anchor='n')

output = tk.Label(lower_frame, font=('Courier', 18), bg='white',
                  anchor='nw', justify='left', bd=4)
output.place(relwidth=1, relheight=1)

root.mainloop()

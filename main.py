from tkinter import *
from tkinter import ttk
import random

TIME = 60
BG = "#333C83"
FONT = "consolas"
TEXT_FONT = "courier new"
SPACE_COUNT = 0
SENTENCE_STRING = ""
sentence = ""


def app():
    global SPACE_COUNT, SENTENCE_STRING, TEXT_FONT, FONT, TIME, BG
    TIME = 60
    BG = "#333C83"
    FONT = "consolas"
    TEXT_FONT = "courier new"
    SPACE_COUNT = 0
    SENTENCE_STRING = ""
    sentence = ""

    # Opening Sentence string from txt file
    def get_sentence():
        global SENTENCE_STRING
        with open("sentences.txt", "r") as file:
            file_contents = file.read()
            # Making a list of sentences
            sentences = file_contents.split("\n")
            new_sentence = random.choice(sentences)

            # Adding the new sentence to the SENTENCE_STRING before displaying
            SENTENCE_STRING += f" {new_sentence}"
            return new_sentence

    def calculate_wpm():
        global sentence, SENTENCE_STRING
        # Formatting input field and making two lists and comparing each word of input list with text list.
        input_text = field.get(1.0, END).replace("\n", " ").strip(" ")
        SENTENCE_STRING = SENTENCE_STRING.strip(" ")
        input_words_list = input_text.split(" ")
        input_words_count = len(input_words_list)
        text_words_list = SENTENCE_STRING.split(" ")
        text_words_list = text_words_list[:input_words_count]
        correct_words = 0
        typos = 0
        for i, word in enumerate(input_words_list):
            if word in text_words_list:
                correct_words += 1
            else:
                print(f"Actual Word: {text_words_list[i]}")
                print(f"Input Word: {word}")
                typos += 1
        return input_words_count, correct_words, typos

    def key_pressed(event):
        global SPACE_COUNT, sentence
        key = event.char
        if key == " " and SPACE_COUNT == 0:
            SPACE_COUNT = 1
            times_up.grid(row=1, column=2, padx=50)
            show_all_grids()
        elif key and SPACE_COUNT == 1:
            field.config(state="normal")
            times_up.grid_forget()
            field.focus()
            count_down(TIME)
            SPACE_COUNT = 2
        elif key == "\r" and SPACE_COUNT == 2:
            sentence = get_sentence()
            text_canvas.itemconfig(sentence_text, text=sentence)

    def show_all_grids():
        press_label.grid_forget()
        icon_canvas.grid_forget()
        canvas.grid(row=1, column=0, columnspan=2)
        text_canvas.grid(row=2, column=1, columnspan=3, pady=(20, 40), padx=50)
        field.grid(row=3, column=1, columnspan=3, padx=50)
        main_heading.grid(row=0, column=1, columnspan=3, pady=(20, 40), padx=50)

    def count_down(sec):
        if sec < 11:
            canvas.itemconfig(timer_text, text=f"{sec}", fill="#FD5D5D")
        canvas.itemconfig(timer_text, text=f"{sec}")

        if sec > 0:
            window.after(1000, count_down, sec - 1)
        else:
            field.config(state="disabled")
            times_up.config(text="Times Up")
            times_up.grid(row=1, column=2, padx=50)
            view_button.grid(row=4, column=2, pady=70, padx=50)

    def show_result():
        wpm, correct_words, typos = calculate_wpm()
        accuracy = correct_words / wpm
        net_speed = accuracy * wpm

        # Showing Result
        main_heading.grid_forget()
        result_label = Label(text="Results", font=(FONT, 30, "bold"), background=BG, foreground="#F24A72")
        result_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), padx=50, sticky="w")

        # Speed label
        speed_label = Label(text="Typing Speed = {} WPM ".format(wpm), background=BG, fg="#FDAF75", font=(FONT, 20))
        speed_label.grid(row=1, column=0, columnspan=2, padx=50, pady=10, sticky="w")

        # ACCURACY Label
        accuracy_label = Label(text="Accuracy     = {:.2f} ({} typos)".format(accuracy * 100, typos),
                               background=BG, fg="#FDAF75", font=(FONT, 20))
        accuracy_label.grid(row=2, column=0, columnspan=2, padx=50, pady=10, sticky="w")

        # Net Speed Label
        net_speed_label = Label(text="Net Speed    = {0:.0f} WPM".format(net_speed),
                                background=BG, fg="#FDAF75", font=(FONT, 20))
        net_speed_label.grid(row=3, column=0, columnspan=2, pady=(0, 20), padx=50, sticky="w")

        # Showing Descriptions

        if net_speed <= 25:
            # Slow Description label
            result_label.config(text="Results (Slow)")
            description_label = Label(text="Slow as a Turtle!", background=BG, fg="#F6F54D", font=(FONT, 30, "bold"))
            description_label.grid(row=4, column=0, columnspan=2, padx=(50, 0))

            # Displaying image
            description_image = PhotoImage(file="images/turtle.png")
            image_label = Label(image=description_image, background=BG)
            image_label.image = description_image
            image_label.grid(row=5, column=0, columnspan=2, padx=(50, 0), sticky="w")

        elif net_speed <= 45:
            # Average Description Label
            result_label.config(text="Results (Average)")
            description_label = Label(text="Typed Like a Rabbit!", background=BG, fg="#DDDDDD", font=(FONT, 30, "bold"))
            description_label.grid(row=4, column=1, columnspan=2)

            # Displaying image
            description_image = PhotoImage(file="images/rabbit.png")
            image_label = Label(image=description_image, background=BG)
            image_label.image = description_image
            image_label.grid(row=5, column=0, columnspan=2, padx=(50, 0), sticky="w")

        elif net_speed <= 65:
            # Fluent Description Label
            result_label.config(text="Results (Fluent)")
            description_label = Label(text="Typed Like an Octopus!", background=BG, fg="#F4BBBB",
                                      font=(FONT, 30, "bold"))
            description_label.grid(row=4, column=1, columnspan=2)

            # Displaying image
            description_image = PhotoImage(file="images/octopus.png")
            image_label = Label(image=description_image, background=BG)
            image_label.image = description_image
            image_label.grid(row=5, column=0, columnspan=2, padx=(50, 0), sticky="w")

        else:
            result_label.config(text="Results (Very Fast)")
            # Fast Description Label
            description_label = Label(text="You type like a Road Runner!", background=BG, fg="#C1F8CF",
                                      font=(FONT, 30, "bold"))
            description_label.grid(row=4, column=1, columnspan=2)

            # Displaying image
            description_image = PhotoImage(file="images/Road Runner.png")
            image_label = Label(image=description_image, background=BG)
            image_label.image = description_image
            image_label.grid(row=5, column=0, columnspan=2, padx=(50, 0), sticky="w")

        try_again_btn.grid(row=5, column=1, sticky="e")

    def view_result():
        canvas.grid_forget()
        text_canvas.grid_forget()
        field.grid_forget()
        view_button.grid_forget()
        times_up.grid_forget()
        show_result()

    def reset():
        window.destroy()
        app()

    window = Tk()
    window.config(padx=50, pady=50, bg=BG)
    window.focus_force()
    window.title("Typing Speed Test")
    window.geometry("700x700")

    # Main Heading
    main_heading = ttk.Label(
        text="Test Your Typing Speed",
        font=(FONT, 30, "bold"),
        background=BG,
        foreground="#F24A72")
    main_heading.grid(row=0, column=1, columnspan=3, pady=(75, 50), padx=50)

    # Creating Canvas to display ICON
    icon_canvas = Canvas(width=400, height=200, bg=BG, highlightthickness=0)
    image = PhotoImage(file="images/icon.png")
    icon_canvas.create_image(200, 100, image=image)
    icon_canvas.grid(row=1, column=1, columnspan=3)

    # Creating Press Label
    press_label = ttk.Label(
        text="Press the  Space button to Start the Test ",
        font=(FONT, 15,), background=BG, foreground="#EAEA7F")
    press_label.grid(row=2, column=1, columnspan=3, pady=(20, 10))
    window.bind('<Key>', key_pressed)

    # Creating Canvas to display Clock
    canvas = Canvas(width=100, height=100, bg=BG, highlightthickness=0)
    img = PhotoImage(file="images/clock.png")
    canvas.create_image(50, 50, image=img)
    canvas.grid_forget()

    # Times UP Label
    times_up = ttk.Label(text="Press any key to Start", font=(FONT, 20), foreground="#FDAF75", background=BG)

    # Clock secs
    timer_text = canvas.create_text(50, 50, text="", font=(FONT, 35, "bold"), fill="#EAEA7F")

    text_canvas = Canvas(width=500, height=100, highlightthickness=0)
    text_image = PhotoImage(file="images/text_box.png")
    text_canvas.create_image(250, 50, image=text_image)
    text_canvas.grid_forget()

    sentence = get_sentence()
    sentence_text = text_canvas.create_text(250, 25, text=sentence, font=(TEXT_FONT, 12), width=480)

    field = Text(height=4, width=60)
    field.config(state="disabled")

    # View Result Button:
    result = PhotoImage(file="images/results.png")
    view_button = Button(text="View Result", image=result, command=view_result)

    try_img = PhotoImage(file="images/try.png")
    try_again_btn = Button(image=try_img,
                           highlightthickness=0, background=BG, command=reset)

    window.mainloop()


if __name__ == '__main__':
    app()

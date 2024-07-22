import tkinter as tk
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='7d19cc448cb7455687639ad82451e9b9')
def get_news():
   # Retrieve the top headlines
   top_headlines = newsapi.get_top_headlines(language='en')

   # Clear the text widget
   text.delete(1.0, tk.END)

   # Display the top headlines
   for article in top_headlines['articles']:
      text.insert(tk.END, article['title'] + '\n\n')
# Create the main window
root = tk.Tk()
root.title('News App')

# Create the text widget
text = tk.Text(root, height=20, width=50)
text.pack()

# Create the button
button = tk.Button(root, text='Get News', command=get_news)
button.pack()

# Run the main loop
root.mainloop()
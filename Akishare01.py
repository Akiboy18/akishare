import os
import socket
import threading
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
import time
import re
import random

# Define combinations for IP/Port conversion
combinations = [
    "ba", "be", "bi", "bo", "bu",
    "ca", "ce", "ci", "co", "cu",
    "da", "de", "di", "do", "du",
    "fa", "fe", "fi", "fo", "fu",
    "ga", "ge", "gi", "go", "gu",
    "ha", "he", "hi", "ho", "hu",
    "ja", "je", "ji", "jo", "ju",
    "ka", "ke", "ki", "ko", "ku",
    "la", "le", "li", "lo", "lu",
    "ma", "me", "mi", "mo", "mu",
    "na", "ne", "ni", "no", "nu",
    "pa", "pe", "pi", "po", "pu",
    'qa', 'qe', 'qi', 'qo', 'qu',
    'ra', 're', 'ri', 'ro', 'ru',
    'sa', 'se', 'si', 'so', 'su',
    'ta', 'te', 'ti', 'to', 'tu',
    'va', 've', 'vi', 'vo', 'vu',
    'wa', 'we', 'wi', 'wo', 'wu',
    'xa', 'xe', 'xi', 'xo', 'xu',
    'ya', 'ye', 'yi', 'yo', 'yu',
    'za', 'ze', 'zi', 'zo', 'zu',
    "ab", "ac", "ad", "af", "ag",
    "ah", "aj", "ak", "al", "am",
    "an", "ap", "aq", "ar", "as",
    "at", "av", "aw", "ax", "ay",
    "az", "eb", "ec", "ed", "ef",
    "eg", "eh", "ej", "ek", "el",
    "em", "en", "ep", "eq", "er",
    "es", "et", "ev", "ew", "ex",
    "ey", "ez", "ib", "ic", "id",
    "if", "ig", "ih", "ij", "ik",
    "il", "im", "in", "ip", "iq",
    "ir", "is", "it", "iv", "iw",
    "ix", "iy", "iz", "ob", "oc",
    "od", "of", "og", "oh", "oj",
    "ok", "ol", "om", "on", "op",
    "oq", "or", "os", "ot", "ov",
    "ow", "ox", "oy", "oz", "ub",
    "uc", "ud", "uf", "ug", "uh",
    "uj", "uk", "ul", "um", "un",
    "up", "uq", "ur", "us", "ut",
    "uv", 'uw', 'ux', 'uy', 'uz'
    "Xa", "Xe", "Xi", "Xo", "Xu",
    "Ya", "Ye", "Yi", "Yo", "Yu",
    "Za", "Ze", "Zi", "Zo", "Zu",
    "Aa", "Ae", "Ai", "Ao", "Au",
    "Ba", "Be", "Bi", "Bo", "Bu",
    "Ca", "Ce", "Ci", "Co", "Cu",
    "Oa", "Oe", "Oi", "Oo", "Ou",
    "Ra", "Re", "Ri", "Ro", "Ru",
    "Ka", "Ke", "Ki", "Ko", "Ku"]

# Port mapping to characters
port_mapping = {
    8000: 'x',
    8001: 'y',
    8002: 'z',
    8003: 'r',
    8004: 's',
    8005: 't',
    8006: 'v',
    8007: 'd',
    8008: 'f',
    8009: 'g',
    8010: 'h'
}


# Function to convert IP and port to a human-readable format
def ip_to_characters(ip_address, port):
    octets = ip_address.split('.')
    result = []

    for octet in octets:
        num = int(octet)
        if 0 <= num < len(combinations):
            result.append(combinations[num])

    # Append the character corresponding to the port number
    result.append(port_mapping[port])

    return ''.join(result)


# Function to convert a human-readable format back to IP and port
def characters_to_ip(characters):
    char_map = {char: idx for idx, char in enumerate(combinations)}

    ip_parts = [characters[i:i + 2] for i in range(0, len(characters) - 1, 2)]

    ip_octets = []

    for part in ip_parts:
        if part in char_map:
            ip_octets.append(str(char_map[part]))

    # Get the last character to determine the port
    last_char = characters[-1]

    # Reverse lookup for port number based on last character
    port_number = next((port for port, char in port_mapping.items() if char == last_char), None)

    return '.'.join(ip_octets), port_number


# Function to handle file sharing
def start_server(ip, port, file_path):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)

    print(f"Server started at {ip}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")

        filename = os.path.basename(file_path)
        conn.send(filename.encode())

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                bytes_to_send = f.read(1024)
                while bytes_to_send:
                    conn.send(bytes_to_send)
                    bytes_to_send = f.read(1024)
            print("File sent successfully.")
        else:
            conn.send(b'ERR: File does not exist on the server.')

        conn.close()


# Function to browse files and send them
def browse_file():
    filename = filedialog.askopenfilename()

    if filename:
        ip = socket.gethostbyname(socket.gethostname())

        # Choose a random port from 8000 to 8010
        port = random.randint(8000, 8000)

        # Start the server in a new thread after selecting the file
        threading.Thread(target=start_server, args=(ip, port, filename), daemon=True).start()

        # Convert IP and Port to string format with appended character
        readable_address = ip_to_characters(ip, port)

        # Display readable address to user
        messagebox.showinfo("Share Code", "Your share code is: " + readable_address)


# Function to start receiving files
def receive_file():
    characters_input = simpledialog.askstring("Input", "Enter the Sender code:")

    if characters_input is None or len(characters_input) == 0:
        return

    ip, port_input = characters_to_ip(characters_input)

    if port_input is None or not (8000 <= port_input <= 8010):
        messagebox.showerror("Error", "Invalid Port Number.")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port_input))

        # Receive the filename first
        filename = client_socket.recv(1024).decode()

        confirm_download = messagebox.askyesno("Confirm Download",
                                               f"File exists: {filename}. Do you want to download it?")

        # Ask user where to save the downloaded file
        save_path = filedialog.asksaveasfilename(defaultextension=".bin",
                                                 initialfile=filename,
                                                 title="Save File",
                                                 filetypes=[("Binary Files", "*.bin"), ("All Files", "*.*")])

        if not save_path:  # If user cancels the dialog
            client_socket.close()
            return

        if confirm_download:
            with open(save_path, 'wb') as f:
                bytes_received = client_socket.recv(1024)
                while bytes_received:
                    f.write(bytes_received)
                    bytes_received = client_socket.recv(1024)

            messagebox.showinfo("File Transfer", "File received successfully.")

        client_socket.close()

    except Exception as e:
        messagebox.showerror("Connection Error", "Could not connect to server.")


# Setting up the GUI
def setup_gui():
    global root

    root = Tk()
    root.title("AkiShare")

    title_label = Label(root, text="AkiShare!", font=("Helvetica", 16))
    title_label.pack(pady=10)
    title_label = Label(root, text="A Minimalistic Sharing application", font=("Helvetica", 10))
    title_label.pack(pady=10)

    Button(root, text="Send File (Start Server)", command=browse_file).pack(pady=10)
    Button(root, text="Receive File (Connect)", command=receive_file).pack(pady=10)
    Button(root, text="Quit Application!", command=root.quit).pack(pady=10)


if __name__ == "__main__":
    setup_gui()
    root.mainloop()
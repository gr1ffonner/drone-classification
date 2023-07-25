import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from drone_separator import classify_drones


class DroneClassifierApp:
    def __init__(self, master):
        self.master = master
        self.input_folder_path = tk.StringVar()
        self.output_folder_path = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Input folder label and button
        input_label = tk.Label(self.master, text="Input Folder:")
        input_label.grid(row=0, column=0, padx=5, pady=5)
        input_button = tk.Button(
            self.master, text="Choose Folder", command=self.choose_input_folder
        )
        input_button.grid(row=0, column=1, padx=5, pady=5)

        # Output folder label and button
        output_label = tk.Label(self.master, text="Output Folder:")
        output_label.grid(row=1, column=0, padx=5, pady=5)
        output_button = tk.Button(
            self.master, text="Choose Folder", command=self.choose_output_folder
        )
        output_button.grid(row=1, column=1, padx=5, pady=5)

        # Run button
        run_button = tk.Button(self.master, text="Run", command=self.run)
        run_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def choose_input_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.input_folder_path.set(folder_path)
            messagebox.showinfo(
                "Input Folder", f"Input folder set to: {self.input_folder_path.get()}"
            )

    def choose_output_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_folder_path.set(folder_path)
            messagebox.showinfo(
                "Output Folder",
                f"Output folder set to: {self.output_folder_path.get()}",
            )

    def run(self):
        input_folder = Path(self.input_folder_path.get())
        output_folder = Path(self.output_folder_path.get())

        if not input_folder.is_dir():
            messagebox.showerror(
                "Invalid Input Folder", "Please choose a valid input folder"
            )
            return

        if not output_folder.is_dir():
            messagebox.showerror(
                "Invalid Output Folder", "Please choose a valid output folder"
            )
            return

        classify_drones(input_folder, output_folder)
        messagebox.showinfo("Complete", "Drone classification complete!")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Drone Classifier")
    app = DroneClassifierApp(root)
    root.mainloop()

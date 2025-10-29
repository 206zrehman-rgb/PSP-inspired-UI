# PSP-inspired-UI

<video src="/Users/zainrehman/Documents/officalProjects/projectVideos" width="320" height="240" controls></video>

A PSP inspired user interface. This interface was made using python along with the Kivy library. Featuring a music player, customisable background as well as a clock which was inspired by the PSP Go clock. The UI is intended to provide a visually pleasing and immersive experience.

Kivy was chosen as the library to build the UI rather then other options such as TKinter and pyQT due to its flexible layouts and widgets, allowing for a design similar to the older look of PSP menus. 

Featuring customisation saved in json in the form of backgrounds being able to be changed and saved for when the next time the application is ran.
<br>
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/4b82ea41-7ef7-489b-8bc8-e4291b1770eb" /> 
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/c2a24d6a-a2f0-4c70-b3b3-852f47601972" />
<br>

<br>
Music can be played from the music submenu, a gif was added to the background add more character to this particular submenu.
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/09054d53-5ff4-4ceb-b6c0-8ca58f1cb660" />
<br>

<br>
The clock feature has a dedicated screen. Using kivys screen manager allowed for transistions between screens as well as control over how the transistion looks. The background is synched to the JSON file too, meaning any changes to the background on the home screen will affect the clock screen.
<br>
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/cd5d2062-0e5c-4e44-8fd6-cba6f616f83b" />
<br>

<br>
The projects main features were split into different files, in order to work on them in detail. They were then imported into the main file. 
<br>

<br>
The tab menu was built using the kivy file, meaning it is part of the background rather then a seperate widget. This was done in order to have it appear throughout all sub menus except the clock feature. The Code for changing the appearance and colour of the tab menu is in the main menu as it is the core of the project and its functionality.
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/b5255ca1-19d6-467c-ba55-0fe5e1f5a750" />
<br>

<br>
Instructions are added in order to help avoid confusion, on submenus that require mouse clicks or space bar clicks more instructions appear
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/4ea89ef7-04fb-4e34-bde4-2543beea54ea" />
<br>


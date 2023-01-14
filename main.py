import pickle

import pandas as pd

# images = pickle.load(open("images.pkl", "rb"))
color = pickle.load(open("color_File.pkl", "rb"))

from PIL import Image as im
import streamlit as st

lis=[
    'Sample-1', 'Sample-2','Sample-3'
]
st.write(
    """
    <div style="margin-align:center;">
    <H1>ColoR Detector Using OpenCV </H1>""",
    unsafe_allow_html=True,
)
st.write(
    """
    <div style="margin-align:center;">
    <H3>Steps To use</H3>
    1) Select Any sample from the Drop Down Menu and Click on the Get Color loaded Button at the bottom.<br>
    2) Look for an Alternate Window & Move to that window.<br>
    3) Double click on the image to get RGB values of the desired color. <br>
    4) Press Escape to close the window.<br>
    
    
    </div>
    """,
    unsafe_allow_html=True,
)

option = st.selectbox('', lis)
col1, col2,col3 = st.columns([5,5,5])
with col1:
    st.markdown(
        """
        <style>
        img {
            float: left;
            height: 200px;
        }        
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.image("download.jpeg", width=200,caption="Sample-1")
with col2:
    st.markdown(
        """
        <style>
        img {
            float: left;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.image("colorful-twisted-candy-18505958.jpg", width=200,caption="Sample-2")
with col3:
    st.markdown(
        """
        <style>
        img {
            float: left;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.image("colorpic.jpg", width=200,caption="Sample-3")
col1, col2,col3 = st.columns([5,5,5])
with col1:
    pass

with col2:
    if st.button("Get Colors Loaded"):
        # st.text("An Alternate Widow is opened. Press Esc to close that window")
        from cv2 import imshow,LINE_AA,imread,EVENT_LBUTTONDBLCLK,namedWindow,WINDOW_NORMAL,resizeWindow,setMouseCallback,rectangle,putText,waitKey,destroyAllWindows

        import pandas as pd

        if option == 'Sample-1':
            img_path = r"sample1.jpeg"
        if option == 'Sample-2':
            img_path = r"sample2.jpg"
        if option == 'Sample-3':
            img_path = r"Sample3.jpg"
        img = imread(img_path)
        clicked = False
        r = g = b = x_pos = y_pos = 0
        csv = pd.DataFrame(color)


        # function to calculate minimum distance from all colors and get the most matching color
        def get_color_name(R, G, B):
            minimum = 10000
            for i in range(len(csv)):
                d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
                if d <= minimum:
                    minimum = d
                    cname = csv.loc[i, "color_name"]
            return cname


        # function to get x,y coordinates of mouse double click
        def draw_function(event, x, y, flags, param):
            if event == EVENT_LBUTTONDBLCLK:
                global b, g, r, x_pos, y_pos, clicked
                clicked = True
                x_pos = x
                y_pos = y
                b, g, r = img[y, x]
                b = int(b)
                g = int(g)
                r = int(r)


        namedWindow('image', WINDOW_NORMAL)
        resizeWindow('image', 600, 800)
        setMouseCallback('image', draw_function)

        while True:

            imshow("image", img)
            if clicked:

                # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
                rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

                # Creating text string to display( Color name and RGB values )
                text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

                # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
                putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, LINE_AA)

                # For very light colours we will display text in black colour
                if r + g + b >= 600:
                    putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, LINE_AA)

                clicked = False

            # Break the loop when user hits 'esc' key
            if waitKey(20) & 0xFF == 27:
                break

        destroyAllWindows()
with col3:
    st.write(
        """
        """,
        unsafe_allow_html=True,
    )









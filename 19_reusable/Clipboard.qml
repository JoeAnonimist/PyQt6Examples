import QtQuick

/*
   Icons taken from the Tango icon project.
*/

Rectangle {
    
    id: clipboard

    height: 50
    width: 180
    color: "darkgray"
    focus: false
    border.width: 0
    border.color: "lightgray"
    
    Keys.onPressed: (e) => {

        if (e.modifiers & Qt.ControlModifier) {
            if (e.key == Qt.Key_X) {
                icon.source = "cut.png"
            } else if (e.key == Qt.Key_C){
                icon.source = "copy.png"
            } else if (e.key == Qt.Key_V){
                icon.source = "paste.png"
            } else {
                icon.source = "keyboard.png"
            }
        } else {
            icon.source = "keyboard.png"
        }
    }

    MouseArea {
    
        anchors.fill: parent
        
        onClicked: {
            parent.focus = ! parent.focus
            if (!parent.focus) {
                border.width = 0
            }
            else {
                border.width = 2
            }
        }
        Image {
            id: icon
            anchors.centerIn: parent
            source: "keyboard.png"
        }
    }
}

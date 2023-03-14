import QtQuick

/* Column positions its children in a row ie. vertically. */

Column {

    spacing: 8
    padding: 8
    
    ColoredRect {
        MouseArea {
            anchors.fill: parent
            onClicked: rotateRect(parent)
        }
     }
    ColoredRect {
        MouseArea {
            anchors.fill: parent
            onClicked: rotateRect(parent)
        }
    }
    ColoredRect {
        MouseArea {
            anchors.fill: parent
            onClicked: rotateRect(parent)
        }
    }
    ColoredRect {
        MouseArea {
            anchors.fill: parent
            onClicked: rotateRect(parent)
        }
    }
    ColoredRect {
        MouseArea {
            anchors.fill: parent
            onClicked: rotateRect(parent)
        }
    }
    ColoredRect {
        MouseArea {
            anchors.fill: parent
            onClicked: rotateRect(parent)
        }
    }
    
    function rotateRect (rect) {
        rect.rotation = rect.rotation + 45
    }
}


import QtQuick

Rectangle {
    
    height: 64
    width: 64
    
    color: Qt.rgba(
        Math.random(),
        Math.random(),
        Math.random(),
        1)
        
    border.color: Qt.lighter(color)
    
    MouseArea {
        anchors.fill: parent
        onClicked: {
            animateRect.target = parent
            animateRect.start()
        }
    }
    
    RotationAnimation {
        id: animateRect
        from: 0
        to: 360
    }
}

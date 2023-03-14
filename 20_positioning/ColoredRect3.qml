
import QtQuick

Rectangle {
    
    signal rectangleClicked(int rect_index)
    
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
        onClicked : parent.rectangleClicked(parent.Positioner.index)
    }
}


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
    
    RotationAnimation on rotation {
        from: 0
        to: 360
    }
}

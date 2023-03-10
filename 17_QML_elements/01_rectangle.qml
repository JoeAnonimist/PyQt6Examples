import QtQuick
import QtQuick.Layouts

Window {

    visible: true
    color: "steelblue"

    RowLayout {
    
        anchors.fill: parent
    
        Rectangle {
            
            Layout.fillWidth: true
            Layout.fillHeight: true
            opacity: 1.0
            color: "red"
            
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    changeOpacity(parent)
                }
            }
        }
        
        Rectangle {

            Layout.fillWidth: true
            Layout.fillHeight: true
            opacity: 1.0
            color: "blue"
            
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    changeOpacity(parent)
                }
            }
        
        }
    }
    
    function changeOpacity(element) {
    
        console.log(element.opacity)

        if (element.opacity > 0.3) {
            element.opacity = element.opacity - 0.1 
        } else {
            element.opacity = 1.0
        }

    }
}

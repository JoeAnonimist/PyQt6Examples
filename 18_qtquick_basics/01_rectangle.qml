import QtQuick

/* Rectangle paints a filled rectangle 
   with an optional border. Use MouseArea
   to handle click events */

Rectangle {
    
    width: 200
    height: 200
    color: "steelblue"
    
    // To make Rectangle handle clicke events
    // need to add MouseArea
    
    MouseArea {
        
        // the MouseArea fills the entire Rectangle
        
        anchors.fill: parent
        
        onClicked: {
            
            // Rectangle is MouseArea parent
            
            if (parent.opacity > 0) {
                parent.opacity = (parent.opacity - 0.2).toFixed(2)
            }
            else {
                parent.opacity = 1.0
            }
        }
    }
}

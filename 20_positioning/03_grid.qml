import QtQuick

/* Place children in a grid */

Grid {

    id: myGrid

    spacing: 8
    padding: 8
    
    rows: 3
    columns: 2
    
    property list<QtObject> rectangles: 
        [rect0, rect1 ,rect2, rect3, rect4, rect5]

    ColoredRect3 {
        id: rect0
        onRectangleClicked: (rect_index) => 
            handleRectangleClick(rect_index)
    }
    
    ColoredRect3 {
        id: rect1
        onRectangleClicked: (rect_index) => 
            handleRectangleClick(rect_index)
    }
    
    ColoredRect3 {
        id: rect2
        onRectangleClicked: (rect_index) => 
            handleRectangleClick(rect_index)
    }
    
    ColoredRect3 {
        id: rect3
        onRectangleClicked: (rect_index) => 
            handleRectangleClick(rect_index)
        }
        
    ColoredRect3 {
        id: rect4
        onRectangleClicked: (rect_index) => 
            handleRectangleClick(rect_index)
    }
    
    ColoredRect3 {
        id: rect5
        onRectangleClicked: (rect_index) => 
            handleRectangleClick(rect_index)
    }

    function handleRectangleClick(rect_index) {

        var source_rect = rectangles[rect_index]
        var dest_rect = (rect_index % 2 == 0) ? 
            rectangles[rect_index + 1] : 
            rectangles[rect_index - 1]
            
        var r = dest_rect.color.r
        var g = dest_rect.color.g
        var b = dest_rect.color.b
        
        dest_rect.color = source_rect.color
        source_rect.color = Qt.rgba(r, g, b, 1)
        
        animateRect.targets = [source_rect, dest_rect]
        animateRect.start()
    }
    
    RotationAnimation {
        id: animateRect
        from: 0
        to: 180
        duration: 250
    }
}

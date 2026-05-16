import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    property int matches: 0
    property int mismatches: 0
    width: 600; height: 200
    color: "#212121"

    Row {
        anchors.centerIn: parent
        spacing: 40

        Rectangle {
            width: 200; height: matches * 10
            color: "green"
            Text { anchors.centerIn: parent; text: "Matches: " + matches }
        }

        Rectangle {
            width: 200; height: mismatches * 10
            color: "red"
            Text { anchors.centerIn: parent; text: "Mismatches: " + mismatches }
        }
    }
}

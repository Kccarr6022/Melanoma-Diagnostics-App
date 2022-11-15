import * as React from "react";
import { View, Text } from "react-native";

export default function HistoryScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <Text
        onPress={() => alert("This is the 'History' screen")}
        style={{ fontSize: 26, fontWeight: "bold" }}
      >
        History Screen
      </Text>
    </View>
  );
}

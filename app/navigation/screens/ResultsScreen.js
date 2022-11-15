import * as React from "react";
import { View, Text } from "react-native";

export default function ResultsScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <Text
        onPress={() => alert("This is the 'Result' screen")}
        style={{ fontSize: 26, fontWeight: "bold" }}
      >
        Result Screen
      </Text>
    </View>
  );
}

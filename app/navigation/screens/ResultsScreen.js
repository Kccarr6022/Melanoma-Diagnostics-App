import * as React from "react";
import { View, Text, StyleSheet } from "react-native";

export default function ResultsScreen({ navigation }) {
  return (
    <View
      style={{
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#1E1E25",
      }}
    >
      <Text
        onPress={() => alert("This is the 'Result' screen")}
        style={styles.textTitle}
      >
        No results to display
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  textTitle: {
    fontSize: 28,
    fontFamily: "DamascusBold",
    fontWeight: "bold",
    padding: 20,
    letterSpacing: 1,
    color: "#C6B5AC",
  },
});

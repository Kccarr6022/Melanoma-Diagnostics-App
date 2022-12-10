import * as React from "react";
import { NavigationContainer, StackActions } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { createStackNavigator } from "@react-navigation/stack";
import Ionicons from "react-native-vector-icons/Ionicons";

// import all Screens
import HomeScreen from "./screens/HomeScreen";
import ResultsScreen from "./screens/ResultsScreen";
import HistoryScreen from "./screens/HistoryScreen";
import TestScreen from "./screens/TestScreen";

// Screen names
const homeName = "Home";
const resultName = "Result";
const historyName = "History";
const testName = "Test";

// Bottom Nav Element
const Tab = createBottomTabNavigator();

function MainContainer() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        // Load app into Home Screen
        initialRouteName={homeName}
        screenOptions={({ route }) => ({
          headerStyle: {
            backgroundColor: "#AF2F32",
            shadowColor: "transparent",
          },
          headerTitleStyle: {
            color: "#AF2F32",
          },
          tabBarStyle: {
            backgroundColor: "#1E1E25",
            borderTopWidth: 0,
          },
          tabBarIcon: ({ focused, size }) => {
            let iconName;
            let rn = route.name;

            /*
             * If    ->    the icon 'focused'              ->  return the highlighted icon
             * Else  ->    return the unhighlighted icon
             */
            if (rn === homeName) {
              if (focused) {
                iconName = "home";
                return (
                  <Ionicons
                    name={iconName}
                    size={(size * 4) / 3}
                    color={"#AF2F32"}
                  />
                );
              } else {
                iconName = "home-outline";
                return (
                  <Ionicons
                    name={iconName}
                    size={(size * 4) / 3}
                    color={"#C6B5AC"}
                  />
                );
              }
            } else if (rn === resultName) {
              if (focused) {
                iconName = "ios-clipboard";
                return (
                  <Ionicons
                    name={iconName}
                    size={(size * 4) / 3}
                    color={"#AF2F32"}
                  />
                );
              } else {
                iconName = "ios-clipboard-outline";
                return (
                  <Ionicons
                    name={iconName}
                    size={(size * 4) / 3}
                    color={"#C6B5AC"}
                  />
                );
              }
            } else if (rn === historyName) {
              if (focused) {
                iconName = "bar-chart";
                return (
                  <Ionicons
                    name={iconName}
                    size={(size * 4) / 3}
                    color={"#AF2F32"}
                  />
                );
              } else {
                iconName = "bar-chart-outline";
                return (
                  <Ionicons
                    name={iconName}
                    size={(size * 4) / 3}
                    color={"#C6B5AC"}
                  />
                );
              }
            } else if (rn === testName) {
              if (focused) {
                iconName = "flask";
                return (
                  <Ionicons
                    name={iconName}
                    size={(size * 4) / 3}
                    color={"#AF2F32"}
                  />
                );
              } else {
                iconName = "flask-outline";
                return (
                  <Ionicons
                    name={iconName}
                    size={(size * 4) / 3}
                    color={"#C6B5AC"}
                  />
                );
              }
            }

            // Return the icon
            return (
              <Ionicons
                name={iconName}
                size={(size * 4) / 3}
                color={"#AF2F32"}
              />
            );
          },
          tabBarShowLabel: false,
        })}
      >
        <Tab.Screen name={homeName} component={HomeScreen} />
        <Tab.Screen name={testName} component={TestScreen} />
        <Tab.Screen name={resultName} component={ResultsScreen} />
        <Tab.Screen name={historyName} component={HistoryScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

export default MainContainer;

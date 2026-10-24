import { StyleSheet, View } from "react-native";

import Button from "../components/Button";
import ScreenTitle from "../components/ScreenTitle";
import { colors, space } from "../theme/tokens";

// Экран-заглушка: форма заказа
export default function OrderFormScreen({ navigation }) {
  return (
    <View style={styles.screen}>
      <ScreenTitle title="Новый заказ" subtitle="Форма заказа. Заглушка." />
      <Button title="Отмена" variant="secondary" onPress={() => navigation.goBack()} />
    </View>
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, padding: space.s4, backgroundColor: colors.background },
});

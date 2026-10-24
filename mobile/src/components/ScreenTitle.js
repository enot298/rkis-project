import { StyleSheet, Text, View } from "react-native";

import { colors, fontSize, space } from "../theme/tokens";

// Заголовок экрана с необязательным пояснением
export default function ScreenTitle({ title, subtitle }) {
  return (
    <View style={styles.wrap}>
      <Text style={styles.title}>{title}</Text>
      {subtitle ? <Text style={styles.subtitle}>{subtitle}</Text> : null}
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: { marginBottom: space.s5 },
  title: { fontSize: fontSize.h1, fontWeight: "700", color: colors.text },
  subtitle: { marginTop: space.s1, fontSize: fontSize.body, color: colors.textMuted },
});

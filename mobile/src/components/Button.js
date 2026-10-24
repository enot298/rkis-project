import { Pressable, StyleSheet, Text } from "react-native";

import { colors, fontSize, radius, space } from "../theme/tokens";

// Базовая кнопка. variant: "primary" | "secondary"
export default function Button({ title, onPress, variant = "primary", disabled = false }) {
  const isPrimary = variant === "primary";
  return (
    <Pressable
      accessibilityRole="button"
      disabled={disabled}
      onPress={onPress}
      style={({ pressed }) => [
        styles.base,
        isPrimary ? styles.primary : styles.secondary,
        pressed && styles.pressed,
        disabled && styles.disabled,
      ]}
    >
      <Text style={[styles.text, isPrimary ? styles.textPrimary : styles.textSecondary]}>
        {title}
      </Text>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  base: {
    minHeight: 48,
    paddingHorizontal: space.s5,
    borderRadius: radius.md,
    alignItems: "center",
    justifyContent: "center",
    borderWidth: 1,
  },
  primary: { backgroundColor: colors.primary, borderColor: colors.primary },
  secondary: { backgroundColor: colors.surface, borderColor: colors.primary },
  pressed: { opacity: 0.85 },
  disabled: { opacity: 0.5 },
  text: { fontSize: fontSize.body, fontWeight: "600" },
  textPrimary: { color: "#FFFFFF" },
  textSecondary: { color: colors.primary },
});

import type { ItemType } from "@/types";
import { READING_ITEM_TYPES, LISTENING_ITEM_TYPES } from "@/types";

export default function itemtypeFromString(text: string): ItemType {
    const allItemTypes =  [...LISTENING_ITEM_TYPES, ...READING_ITEM_TYPES]

    // Return text as-is if valid ItemType (is uppercased)
    if (allItemTypes.includes(text as ItemType)) return text as ItemType;

    // Check if text (lowercased) is valid ItemType
    const itemTypeMap: Record<string, ItemType> = {}
    for (const item of allItemTypes) {
        itemTypeMap[item.toLowerCase()] = item
    }

    const result = itemTypeMap[text]
    if (result == undefined) {
        throw new Error("Unknown item type.")
    }
    return result
}
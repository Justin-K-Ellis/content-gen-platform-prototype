import {describe, it, expect} from "vitest"
import itemtypeFromString from "@/core/itemtypeFromString"

describe("itemTypeFromString func", () => {
    it("converts a lowercase string into the corresponding ItemType", () => {
        const itemStr: string = "ra"
        const result = itemtypeFromString(itemStr)
        expect(result).toEqual("RA")
    })

    it("returns the original ItemType when passed an uppercase str", () => {
        const itemStr: string = "RA"
        const result = itemtypeFromString(itemStr)
        expect(result).toEqual("RA")
    })

    it("throws when passed an invalid ItemType", () => {
        const itemStr: string = "XA"
        expect(() => itemtypeFromString(itemStr)).toThrow(`${itemStr} is not a valid item type.`)
    })
})
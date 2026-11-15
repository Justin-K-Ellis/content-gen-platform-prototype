export interface LinkData {
    url: string
    text: string
}

export const READING_ITEM_TYPES = ["RA", "RBSK", "RBSC", "RC"] as const;
export const LISTENING_ITEM_TYPES = ["LA", "LB", "LC", "LD"] as const;

export type ReadingItemType = typeof READING_ITEM_TYPES[number];
export type ListeningItemType = typeof LISTENING_ITEM_TYPES[number];
export type ItemType = ReadingItemType | ListeningItemType; 

export interface RACreate {
    stem: string,
    options: string[]
    key: string
}

export interface RAPublic extends RACreate {
    public_id: string
}

export type ItemCreate = RACreate
export type ItemPublic = RAPublic

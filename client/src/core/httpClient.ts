import type {ItemCreate, ItemPublic} from "@/types"

interface IHttpClient {
    getOne: (url: string) => ItemPublic 
    getAll: (url: string) => ItemPublic[]
    postOne: (url: string, item: ItemCreate) => ItemPublic
    postMany: (url: string, items: ItemCreate[]) => ItemPublic[]
    putOne: (url: string, public_id: string) => ItemPublic
    putMonay: (url: string, public_ids: string[]) => ItemPublic[]
    deleteOne: (url: string, public_id: string) => void
    deleteMany: (url: string, public_id: string) => void
    setBaseUrl: (url: string) => void
}
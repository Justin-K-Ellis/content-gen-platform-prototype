import type {ItemCreate, ItemPublic, ItemType} from "@/types"

interface IHttpClient {
    // getOne: (path: string) => ItemPublic 
    // getAll: (path: string) => ItemPublic[]
    createOne: (type: ItemType, prompt: string) => Promise<ItemCreate>
    createMany: (type: ItemType, count: number) => Promise<ItemCreate[]>
    // putOne: (url: string, public_id: string) => ItemPublic
    // putMonay: (url: string, public_ids: string[]) => ItemPublic[]
    // deleteOne: (url: string, public_id: string) => void
    // deleteMany: (url: string, public_id: string) => void
    // setBaseUrl: (url: string) => void
}

class HttpClient implements IHttpClient {
    private baseUrl: string

    constructor(baseUrl: string) {
        this.baseUrl = baseUrl
    }

    setBaseUrl(url: string) {
        const urlObject = new URL(url)
        this.baseUrl = urlObject.href
    }

    async createOne(type: ItemType, prompt: string): Promise<ItemCreate> {
        const url = new URL(type.toLowerCase(), this.baseUrl)
        const response = await fetch(url.href, {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify({
                query: prompt
            })
        })
        const data: ItemCreate = await response.json()
        return data
    }

    async createMany(type: ItemType, count: number): Promise<ItemCreate[]> {
        const url = this.baseUrl + `${type.toLowerCase()}/batch?count=${count}`
        const validated_url = new URL(url)
        const response = await fetch(validated_url.href, {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            }
        })
        const data: ItemCreate[] = await response.json()
        return data
    }
}

export default HttpClient
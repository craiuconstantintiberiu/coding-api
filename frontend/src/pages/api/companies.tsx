import type {NextApiRequest, NextApiResponse} from 'next'
import {fetch} from "next/dist/compiled/@edge-runtime/primitives/fetch";

type Company = {
    company_id: number,
    name: string,
    country: string,
    founding_date: string,
    description: string
}

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse<Array<Company>>
) {
    console.log("asdasd")
    let data = await fetch("api:20002/api/companies",
        {
            method: "GET",
            headers: {
            "Content-Type": "text/plain"
        }
        })
    let json = await data.json()
    res.status(200)
    res.send(json)
}
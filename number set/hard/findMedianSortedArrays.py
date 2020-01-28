from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if nums1_len == 0:
            if nums2_len % 2 == 0:
                mid = int(nums2_len/2)
                ret = nums2[mid]+nums2[mid-1]
                ret /= 2.0
            else:
                ret  = float(nums2[int((nums2_len+1)/2)-1])
        elif nums2_len == 0:
            if nums1_len % 2 == 0:
                mid = int(nums1_len/2)
                ret = nums1[mid]+nums1[mid-1]
                ret /= 2.0
            else:
                ret  = float(nums1[int((nums1_len+1)/2)-1])
        else:
            count = 0
            dest = []
            all_len = nums1_len + nums2_len
            if all_len % 2 == 0:  #not_odd
                lmid = int(all_len / 2)
                rmid = lmid + 1
                i = 0
                j = 0
                while True:
                    if len(nums1) != 0 and len(nums2)!=0:
                        if nums1[i] <= nums2[j]:
                            dest.append(nums1[i])
                            #if i < nums1_len - 1:
                            nums1 = nums1[1:]
                            #i += 1
                            count += 1
                        else:
                            if len(nums2) != 0:
                                dest.append(nums2[j])
                                #if j < nums2_len - 1:
                                nums2 = nums2[1:]
                                #j += 1
                                count += 1
                    elif len(nums1) == 0 and len(nums2)!=0:
                        dest.append(nums2[j])
                        nums2 = nums2[1:]
                        count += 1
                    else:
                        dest.append(nums1[j])
                        nums1 = nums1[1:]
                        count += 1
                    if count == lmid:
                        # if nums1[i]<=nums2[j]:
                        #     dest.append(nums1[i])
                        # else:
                        #     dest.append(nums2[j])
                        # if i == 0:
                        #     dest.append(nums1[i])
                        # elif j == 0:
                        #     dest.append(nums2[j])
                        if len(nums1) != 0 and len(nums2) == 0:
                            dest.append(nums1[0])
                        elif len(nums2) != 0 and len(nums1) == 0:
                            dest.append(nums2[0])
                        else:
                            x = min(nums1[0],nums2[0])
                            dest.append(x)
                        ret = dest[lmid-1] + dest[rmid-1]
                        ret /= 2
                        break
            else:
                mid = int(all_len / 2) + 1
                dest=[]
                while True:
                    if len(nums1) != 0 and len(nums2) != 0:
                        if nums1[0]<=nums2[0]:
                            dest.append(nums1[0])
                            nums1=nums1[1:]
                            count += 1
                        elif nums1[0]>=nums2[0]:
                            dest.append(nums2[0])
                            nums2 = nums2[1:]
                            count += 1
                    elif len(nums1) == 0 and len(nums2)!=0:
                        dest.append(nums2[0])
                        nums2 = nums2[1:]
                        count += 1
                    else:
                        dest.append(nums1[0])
                        nums1 = nums1[1:]
                        count += 1
                    if count == mid:
                        ret = float(dest[count-1])
                        break
        return ret

s = Solution()
print(s.findMedianSortedArrays([2],[1,3,4,5]))
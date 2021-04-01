from rest_framework import pagination
from rest_framework.response import Response


class CourseListPagination(pagination.LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'current_page': self.offset,
            'total_pages': self.count,
            'results': data
        })
